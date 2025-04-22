#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify

app = Flask(__name__)

# 模擬資料庫：存放加班紀錄
overtime_data = {
    "A123456": [
        {"date": "2025-04-10", "hours": 4},
        {"date": "2025-04-12", "hours": 2}
    ]
}

# ➕ 基礎路由
@app.route('/v1/demo/hr', methods=['GET'])
def base_hr():
    return jsonify({"message": "HR API is running!"})

# 查詢加班紀錄
@app.route('/v1/demo/hr/<emp_id>/overtime-stats', methods=['GET'])
def get_overtime(emp_id):
    records = overtime_data.get(emp_id, [])
    total_hours = sum(r['hours'] for r in records)
    return jsonify({
        "employeeId": emp_id,
        "totalHours": total_hours,
        "records": records
    })

# 申請加班（支援 單筆 or 多筆 JSON）
@app.route('/v1/demo/hr/<emp_id>/overtime', methods=['POST'])
def apply_overtime(emp_id):
    print("🔹 Headers:", request.headers)
    print("🔹 Raw body:", request.data)
    data = request.get_json(silent=True)
    print("🔹 Parsed data type:", type(data))
    print("🔹 Parsed data:", data)

    if data is None:
        return jsonify({"error": "未收到有效 JSON"}), 400

    records_added = []

    # 支援多筆資料（list）
    if isinstance(data, list):
        for item in data:
            record = {
                "date": item.get("startTime", "")[:10],
                "hours": float(item.get("hours", 0))
            }
            overtime_data.setdefault(emp_id, []).append(record)
            records_added.append(record)
        return jsonify({"message": "加班申請成功（多筆）", "records": records_added}), 201

    # 支援單筆資料（dict）
    elif isinstance(data, dict):
        record = {
            "date": data.get("startTime", "")[:10],
            "hours": float(data.get("hours", 0))
        }
        overtime_data.setdefault(emp_id, []).append(record)
        return jsonify({"message": "加班申請成功", "record": record}), 201

    else:
        return jsonify({"error": "不支援的資料格式"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
