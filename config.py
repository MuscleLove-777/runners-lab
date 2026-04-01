"""ランナーズラボ - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "ランナーズラボ"
BLOG_DESCRIPTION = "マラソン・ランニング・有酸素運動の科学と実践ガイド"
BLOG_URL = "https://musclelove-777.github.io/runners-lab"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/runners-lab"

TARGET_CATEGORIES = [
    "ランニングフォーム",
    "マラソントレーニング",
    "HIIT・インターバル",
    "心肺機能強化",
    "ランニングギア",
]

THEME = {
    "primary": "#2563eb",
    "accent": "#38bdf8",
    "gradient_start": "#2563eb",
    "gradient_end": "#0ea5e9",
    "dark_bg": "#0a0f20",
    "dark_surface": "#151d35",
    "light_bg": "#eff6ff",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 2500
ARTICLES_PER_DAY = 2
SCHEDULE_HOURS = [5, 17]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.0-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.0-flash-lite"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 70
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "ランニングシューズ": [
        {"service": "Amazon ランニングシューズ", "url": "https://www.amazon.co.jp", "description": "ランニングシューズ各種"},
        {"service": "楽天市場 シューズ", "url": "https://www.rakuten.co.jp", "description": "ランニングシューズお得情報"},
    ],
    "ランニングウォッチ": [
        {"service": "Amazon Garmin", "url": "https://www.amazon.co.jp", "description": "GarminランニングGPS"},
        {"service": "Amazon Apple Watch", "url": "https://www.amazon.co.jp", "description": "Apple Watchフィットネス"},
    ],
    "ウェア・ギア": [
        {"service": "Amazon ランニングウェア", "url": "https://www.amazon.co.jp", "description": "ランニングウェア"},
        {"service": "楽天市場 スポーツ", "url": "https://www.rakuten.co.jp", "description": "スポーツウェア"},
    ],
    "サプリ・栄養": [
        {"service": "Amazon BCAA", "url": "https://www.amazon.co.jp", "description": "ランナー向けサプリ"},
        {"service": "マイプロテイン", "url": "https://www.myprotein.jp", "description": "エンデュランス系サプリ"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
DASHBOARD_PORT = 8080

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-CSFVD34MKK"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
