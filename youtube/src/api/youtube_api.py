from googleapiclient.discovery import build
import datetime

API_KEY = "AIzaSyBt8MQRZBsi4TMdt3jyOU2PUbRdYitqacM"  # Thay bằng API Key của bạn
youtube = build("youtube", "v3", developerKey=API_KEY)

def get_youtube_stats(video_id):
    try:
        request = youtube.videos().list(
            part="statistics,snippet",  # Đảm bảo có "snippet" để lấy title
            id=video_id
        )
        response = request.execute()
        if not response["items"]:
            return None

        video = response["items"][0]
        stats = {
            "video_id": video_id,
            "title": video["snippet"]["title"],  # Lấy title từ snippet
            "likes": int(video["statistics"].get("likeCount", 0)),
            "views": int(video["statistics"].get("viewCount", 0)),
            "comments": int(video["statistics"].get("commentCount", 0)),
            "timestamp": datetime.datetime.now().isoformat()
        }
        return stats
    except Exception as e:
        print(f"Lỗi khi gọi API: {e}")
        return None