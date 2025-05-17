# src/cli/interface.py
from src.api.youtube_api import get_youtube_stats


def run_cli():
    print("=== YouTube Stats Collector ===")
    # TODO: Get links from database
    while True:
        print("\n1. Lấy thông tin video")
        print("2. Thoát")
        choice = input("Chọn (1-2): ")

        if choice == '1':
            video_id = input("Nhập YouTube Video ID (hoặc URL): ")
            if 'youtube.com' in video_id or 'youtu.be' in video_id:
                video_id = video_id.split('v=')[-1].split('&')[0] if 'v=' in video_id else video_id.split('/')[-1]

            stats = get_youtube_stats(video_id)
            if stats:
                # TODO: Save to database
                print(f"Thông tin video {video_id}:")
                print(f"Title: {stats['title']}")
                print(f"Likes: {stats['likes']}")
                print(f"Views: {stats['views']}")
                print(f"Comments: {stats['comments']}")
                print(f"Timestamp: {stats['timestamp']}")



        elif choice == '3':
            print("Đã thoát chương trình!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")