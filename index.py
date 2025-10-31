from flask import Flask, request, jsonify
import requests

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
    
    # ---- API nguồn thật của bạn ----
    # Bạn có thể đổi API này sang API FreeFire bạn dùng thật
    api_url = f"https://vduy-like-ff.vercel.app/like?uid{uid} "
    
    try:
        r = requests.get(api_url, timeout=10)
        data = r.json()
    except Exception as e:
        return jsonify({"error": f"Failed to fetch data: {str(e)}"})

    # ---- Kiểm tra dữ liệu trả về ----
    if "LikesAfterCommand" not in data:
        return jsonify({"error": "Invalid UID or API returned no data", "raw": data})
    
    # ---- Trích xuất dữ liệu thật ----
    uid = data.get("UID", uid)
    name = data.get("PlayerNickname", "Unknown")
    likes_before = data.get("LikesBeforeCommand", 0)
    likes_after = data.get("LikesAfterCommand", 0)
    given = data.get("LikesGivenByAPI", 0)

    return jsonify({
        "UID": uid,
        "Name": name,
        "LikesBefore": likes_before,
        "LikesAfter": likes_after,
        "GivenByAPI": given,
        "status": "success"
    })

if __name__ == '__main__':
    app.run()
