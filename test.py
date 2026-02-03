import os

def get_database_url():

    return os.getenv("DATABASE_URL", "http://localhost:5432")

if __name__ == "__main__":
    url = get_database_url()
    print(f"✅ 系統啟動中... 連線至：{url}")
