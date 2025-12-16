# config.py - تنظیمات ثابت

import os

# توکن از Environment Variable (در Render امن اضافه می‌شه)
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found! Add it in Render Environment Variables")

# ساعت‌های زمان‌بندی (به وقت ایران)
REPORT_HOUR = 21  # ساعت ۲۱:۰۰ شروع گزارش‌گیری
PLAN_HOUR = 22     # ساعت ۲۲:۰۰ ارسال برنامه فردا

# لینک گروه‌ها
group_links = {
    "ادبیات": "https://t.me/+71ZwjKDd7jAzZWE0",    # لینک واقعی گروه فیزیک
    "انگلیسی":   "https://t.me/+eTRhZPFrhFo4Y2M8",
    "دینی":  "https://t.me/+ngnkz1wErBg2NzFk",
    "عربی":   "https://t.me/+0Mq-o9GCmcwwYWE0",
}
