import undetected_chromedriver as uc
import time
import random

def run_bot():
    print("[+] جاري تشغيل المتصفح المتخفي والتجهيز للسيرفر...")
    
    options = uc.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1280,720')
    
    driver = uc.Chrome(options=options)
    
    try:
        # رابط مقطعك مدمج جاهز
        VIDEO_URL = "https://youtu.be/Jcegn1paM7g?si=X__yXMzRkueEtilq"
        
        print(f"[+] الدخول إلى رابط الفيديو مباشرة: {VIDEO_URL}")
        driver.get(VIDEO_URL)
        
        # وقت مشاهدة عشوائي ليناسب طول مقطعك
        watch_duration = random.randint(90, 160) 
        print(f"[+] تم فتح مقطعك بنجاح. جاري المحاكاة والمشاهدة لمدة {watch_duration} ثانية...")
        
        start_time = time.time()
        while time.time() - start_time < watch_duration:
            # محاكاة حركة التمرير العشوائي
            scroll_amount = random.randint(150, 400)
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(random.randint(7, 12))
            driver.execute_script(f"window.scrollBy(0, -{int(scroll_amount/2)});")
            time.sleep(random.randint(9, 15))
            
        print("[+] تمت المشاهدة بنجاح وإنهاء المهمة بالتنظيف.")
        
    except Exception as e:
        print(f"[-] حدث خطأ أثناء التشغيل: {e}")
        
    finally:
        driver.quit()
        print("[+] تم إغلاق المتصفح وجلسة السيرفر السحابي بأمان.")

if __name__ == "__main__":
    run_bot()
