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

# ➕ 補上這個基礎路由
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

# 申請加班
@app.route('/v1/demo/hr/<emp_id>/overtime', methods=['POST'])
def apply_overtime(emp_id):
    print("收到加班申請 POST！")
    data = request.get_json(silent=True)
    print("收到的資料：", data)

    if data is None:
        return jsonify({"error": "未收到有效 JSON 資料"}), 400

    record = {
        "date": data.get("startTime")[:10],
        "hours": data.get("hours")
    }
    overtime_data.setdefault(emp_id, []).append(record)
    return jsonify({"message": "加班申請成功", "record": record}), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

