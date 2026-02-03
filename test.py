import os

def get_database_url():
    """
    獲取資料庫連線網址。
    在解衝突作業中，不同分支將會對這行有不同的期待。
    """
    
<<<<<<< HEAD
    DATABASE_URL = "http://localhost:5432" 
=======
    DATABASE_URL = "http://localhost:8080" 
>>>>>>> 62263c909cf6901f71e50167c8e45245b3e4b8e0
    
    return DATABASE_URL

if __name__ == "__main__":
    url = get_database_url()
    print(f"✅ 系統啟動中... 連線至：{url}")