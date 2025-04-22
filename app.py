#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify

app = Flask(__name__)

# 模擬的員工通訊錄資料
employee_directory = [
    # 同名同姓：王大明 (5人)
    {"name": "王大明", "employeeId": "A100001", "extension": "1001", "email": "daming1@corp.com", "department": "資訊部"},
    {"name": "王大明", "employeeId": "A100002", "extension": "1002", "email": "daming2@corp.com", "department": "人資部"},
    {"name": "王大明", "employeeId": "A100003", "extension": "1003", "email": "daming3@corp.com", "department": "財務部"},
    {"name": "王大明", "employeeId": "A100004", "extension": "1004", "email": "daming4@corp.com", "department": "營運部"},
    {"name": "王大明", "employeeId": "A100005", "extension": "1005", "email": "daming5@corp.com", "department": "行銷部"},

    # 其他隨機員工 (25筆)
    {"name": "李小美", "employeeId": "A100006", "extension": "1006", "email": "xiaomei@corp.com", "department": "人資部"},
    {"name": "陳志偉", "employeeId": "A100007", "extension": "1007", "email": "zhiwei@corp.com", "department": "研發部"},
    {"name": "林雅婷", "employeeId": "A100008", "extension": "1008", "email": "yating@corp.com", "department": "客服部"},
    {"name": "張書豪", "employeeId": "A100009", "extension": "1009", "email": "shuhao@corp.com", "department": "財務部"},
    {"name": "黃婉君", "employeeId": "A100010", "extension": "1010", "email": "wanjun@corp.com", "department": "行銷部"},

    {"name": "許乃文", "employeeId": "A100011", "extension": "1011", "email": "naiwen@corp.com", "department": "營運部"},
    {"name": "趙心怡", "employeeId": "A100012", "extension": "1012", "email": "xinyi@corp.com", "department": "客服部"},
    {"name": "吳建宏", "employeeId": "A100013", "extension": "1013", "email": "jianhong@corp.com", "department": "資訊部"},
    {"name": "何文龍", "employeeId": "A100014", "extension": "1014", "email": "wenlong@corp.com", "department": "法務部"},
    {"name": "戴淑芬", "employeeId": "A100015", "extension": "1015", "email": "shufen@corp.com", "department": "財務部"},

    {"name": "孫健誠", "employeeId": "A100016", "extension": "1016", "email": "jiancheng@corp.com", "department": "人資部"},
    {"name": "賴宜君", "employeeId": "A100017", "extension": "1017", "email": "yijun@corp.com", "department": "行銷部"},
    {"name": "張詠翔", "employeeId": "A100018", "extension": "1018", "email": "yongxiang@corp.com", "department": "研發部"},
    {"name": "簡麗華", "employeeId": "A100019", "extension": "1019", "email": "lihua@corp.com", "department": "客服部"},
    {"name": "朱彥廷", "employeeId": "A100020", "extension": "1020", "email": "yanting@corp.com", "department": "資訊部"},

    {"name": "劉佩君", "employeeId": "A100021", "extension": "1021", "email": "peijun@corp.com", "department": "人資部"},
    {"name": "廖聖傑", "employeeId": "A100022", "extension": "1022", "email": "shengjie@corp.com", "department": "營運部"},
    {"name": "郭怡君", "employeeId": "A100023", "extension": "1023", "email": "yijun.k@corp.com", "department": "法務部"},
    {"name": "潘俊宇", "employeeId": "A100024", "extension": "1024", "email": "junyu@corp.com", "department": "客服部"},
    {"name": "曾惠婷", "employeeId": "A100025", "extension": "1025", "email": "huiting@corp.com", "department": "行銷部"},

    {"name": "馮彥斌", "employeeId": "A100026", "extension": "1026", "email": "yanbin@corp.com", "department": "研發部"},
    {"name": "韓玉琳", "employeeId": "A100027", "extension": "1027", "email": "yulin@corp.com", "department": "資訊部"},
    {"name": "陳盈潔", "employeeId": "A100028", "extension": "1028", "email": "yingjie@corp.com", "department": "人資部"},
    {"name": "楊文凱", "employeeId": "A100029", "extension": "1029", "email": "wenkai@corp.com", "department": "財務部"},
    {"name": "許育豪", "employeeId": "A100030", "extension": "1030", "email": "yuhao@corp.com", "department": "營運部"}
]

@app.route('/v1/employee/contact', methods=['GET'])
def get_employee_contact():
    query = request.args.get("query", "").strip()
    if not query:
        return jsonify({"error": "請提供查詢參數 query，例如員工 ID 或姓名"}), 400

    # 查詢符合的資料
    results = [emp for emp in employee_directory if query in emp["name"] or query in emp["employeeId"]]

    if not results:
        return jsonify({"message": f"查無與 '{query}' 相關的員工資料"}), 404

    # 回傳第一筆（或全部也可以，視需求）
    return jsonify(results[0])

# 測試基本路由
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Employee Contact API is running!"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
