from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Like API is running ✅",
        "status": "online"
    })

@app.route('/like')
def like():
    uid = request.args.get("uid")
    if not uid:
        return jsonify({"error": "Missing UID"})
    
    # ----- Giả lập dữ liệu API -----
    player_name = "FB:ㅤ@GMRemyX"  # bạn có thể thay thành dữ liệu thật nếu có API riêng
    likes_before = 1000
    likes_after = 1020
    given = likes_after - likes_before

    return jsonify({
        "UID": uid,
        "Name": player_name,
        "LikesBefore": likes_before,
        "LikesAfter": likes_after,
        "GivenByAPI": given,
        "status": "success"
    })

if __name__ == '__main__':
    app.run()
