import tkinter as tk
from tkinter import filedialog
import os

# Ijad Root
win=tk.Tk()
win.geometry("1200x650")
win.resizable(False,False)
win.config(bg="#4D4646")  #background panels

# list baraye garar dadan soalat 
sovalat=[" ترجیح میدهم تنها بوده و مشغول کار خود باشم(1","2) خودم را به همه معرفی میکنم","3) همیشه از صحت آنچه که میگویم یا به آن معتقد هستم اطمینان حاصل میکنم","4) اغلب میتوانم بدون فکر زیاد عمل کنم و حرف بزنم","5) نمی توانم ذهنم را از مشکلات آزاد کنم","6) برای کار ها یا مواردی که دشوار هستند زمان کافی را به منظور کسب آمادگی لازم اختصاص میدهم","7) اگر حرفی برای گفتن داشته باشم هیچکس نمیتواند مانع از ابراز نظرم بشود","8) وقتی که فرد دیگری رهبری را به دست میگیرد و شخص اول میشود برای من کاملا خوش آیند است","9) هر کاری را که خیلی با کارهای دوستانم متفاوت باشد دوست ندارم انجام دهم","10) احساسات دیگران برای من تاثیر میگذارد","11) همیشه مطمئن میشوم که کاری که انجام داده ام به بهترین نحو ممکن انجام شده است","12) به سرعت مشکلات دیگران را متوجه میشوم","13) اگر ممکن باشد ترجیح میدهم احساسات را کنار بگذارم","14) معمولا عجولانه به چیزی واکنش نشان نمی دهم","15) هنگامی که در کنار دیگران کار میکنم(کارگروهی) در بهترین و کارا ترین وضعیت خود هستم","16) بیرون رفتن را خیلی دوست ندارم","17) داشتن تفریح و سرگرمی در اوقات فراغت برایم مهم است","18) به شیوه‌ای که دیگران احساس میکنند توجهی ندارم","19) به راحتی کسل و بی حوصله میشوم","20) در مقایسه با دیگران آدم کمتر حساسی هستم","21) از بین بردن اعتماد به نفس من کار بسیار دشواری است","22) همیشه انجام کار های جدید و متفاوت مرا به خود جذب میکند","23) سرگرم کردن دوستان یکی از کارهای مورد علاقه من است","24) من هر گونه احساسات رنجش و آزردگی را کنترل میکنم","25) همیشه عقایدم را ابراز میکنم","26) فکر کردن به اتفاقات و رویداد های گذشته خیلی مرا به خود مشغول میکند","27) در جستجوی افرادی برای بودن با آنها نیستم","28) آدم قانع و رضایت‌مندی هستم","29) به راحتی و به تنهایی میتوانم تصمیم بگیرم","30) علاقه‌مند نیستم دیگران را قانع کنم که نظر یا عقیده‌شان را تغییر دهم","31) برایم دشوار نیست که به کاری بچسبم و تا آخر آنرا ادامه دهم","32) فورا و در لحظه نظرم را عوض کنم","33) هنگامی که افراد دور هم جمع میشوند معمولا کسی که دیگران را درگیر جمع میکند من هستم","34) در اعتماد به نفس بخشیدن به دوستانم هیچ ضرری نمی بینم","35) دیگران مرا به عنوان فردی فهیم و باهوش میشناسند","36) معمولا اگر فردی در مورد چیزی احساس شدیدی داشته باشد من نیز با او موافق هستم","37) معمولا در مباحثات و مکالمات من پیروز میشوم","38) داشتن دوست برایم خیلی مهم نیست","39) دوست ندارم دیگران وارد حریم من بشوند یا در کارهایم سرک بکشند","40) دوست دارم دیگران هر وقت که خواستند با من تماس بگیرند ","press kry for computing"]
# add type haye shakhsiyati
type_of_sovalat = ["SO","A","F","SP","I","D","A","P","G",'I',"D","I","F","D","G","P","SP","F","SP","F","F","SP","G","P","A","I","SO","D","SO","P","D","SP","A","G","I","P","A","SO","SO","G"," "]
# baraye controll peymayesh dakhel list ha 
x=1
step=0
bool_check=False
num=0
global text
text=" "

answers=[] #list baraye negah dari va zakhire pasokh ha !!

# function baraye mohasebe va chap type shakhsiyati va taen harfe mosalat
def Computing():
    global name_note_txt
    global text
    global notesave
    global file_path
    type_SO = [answers[0],answers[26],answers[28],answers[37],answers[38]]  # tartib dehi be type ha
    sum_type_SO = sum(type_SO)  # jam kardan type baraye motagayer tafrig anha
    type_G = [answers[8],answers[14],answers[22],answers[33],answers[39]] # tartib dehi be type ha
    sum_type_G = sum(type_G)  # jam kardan type baraye motagayer tafrig anha
    type_A = [answers[1],answers[6],answers[24],answers[32],answers[36]] # tartib dehi be type ha
    sum_type_A = sum(type_A)  # jam kardan type baraye motagayer tafrig anha
    type_P = [answers[7],answers[15],answers[23],answers[29],answers[35]] # tartib dehi be type ha
    sum_type_P = sum(type_P)  # jam kardan type baraye motagayer tafrig anha
    type_I = [answers[4],answers[9],answers[11],answers[25],answers[34]] # tartib dehi be type ha
    sum_type_I = sum(type_I)  # jam kardan type baraye motagayer tafrig anha
    type_F = [answers[2],answers[12],answers[17],answers[19],answers[20]] # tartib dehi be type ha
    sum_type_F = sum(type_F)  # jam kardan type baraye motagayer tafrig anha
    type_SP = [answers[3],answers[16],answers[18],answers[21],answers[31]] # tartib dehi be type ha
    sum_type_SP = sum(type_SP)  # jam kardan type baraye motagayer tafrig anha
    type_D = [answers[5],answers[10],answers[13],answers[27],answers[30] ] # tartib dehi be type ha
    sum_type_D = sum(type_D)  # jam kardan type baraye motagayer tafrig anha

    # tafrig type ha baraye yaftane harf mosalat
    tafrig_SO_G = sum_type_SO - sum_type_G     
    tafrig_A_P = sum_type_A - sum_type_P
    tafrig_I_F = sum_type_I - sum_type_F
    tafrig_SP_D = sum_type_SP - sum_type_D

    # taen harf mosalat
    if tafrig_SO_G < 0:
        mosalat_SO_G = "G"
    else:
        mosalat_SO_G = "SO"

    if tafrig_A_P < 0:
        mosalat_A_P = "P"
    else:
        mosalat_A_P = "A"

    if tafrig_I_F < 0:
        mosalat_I_F = "F"
    else:
        mosalat_I_F = "I"

    if tafrig_SP_D < 0:
        mosalat_SP_D = "D"
    else:
        mosalat_SP_D = "SP"    





    # chap type shakhs 
    if mosalat_I_F=="F" and mosalat_SP_D=="D" and mosalat_A_P=="A" and mosalat_SO_G=="G":
        text="""
        FDAG _ رئیس
        ویژگی ها: واقع‌گرا، مشرف بر خود، خودبیان‌گر و معاشرتی
        مشاغل: افسر نیروهای نظامی، مدیر بانک، مدیر باشگاه، مدیر هتل، مدیر
        تولید، مدیر شعبه‌ی فروش، مدیر حمل و نقل 
        """
        with open(file_path, "a", encoding="utf-8") as notesave:
            notesave.write(text)        
        labtext.set(text)
    elif mosalat_I_F=="F" and mosalat_SP_D=="SP" and mosalat_A_P=="A" and mosalat_SO_G=="G":
        text="""
        FSpAG _ فرصت‌طلب
        ویژگی ها: واقع‌گرا، خودانگیخته، خودبیان‌گر و معاشرتی            
        مشاغل: مدیر تبلیغات، متصدی حراج، منشی اداری، مشاور
        املاک، مدیر روابط عمومی
        """
        with open(file_path, "a", encoding="utf-8") as notesave:
            notesave.write(text)        
        labtext.set(text)
    elif mosalat_I_F=="I" and mosalat_SP_D=="D" and mosalat_A_P=="A" and mosalat_SO_G=="G":
        text="""
        IDAG _ مربی
        ویژگی ها: خیال‌پرداز، مشرف بر خود، خودبیان‌گر و معاشرتی
        مشاغل: پزشک، متخصص بیماری‌های استخوان، روان‌شناس، پرستار
        ارشد، معلم، فعال اجتماعی، سرپرست اردوهای جوانان
        """

        with open(file_path, "a", encoding="utf-8") as notesave:
         notesave.write(text)        
        labtext.set(text) 
    elif mosalat_I_F=="I" and mosalat_SP_D=="SP" and mosalat_A_P=="A" and mosalat_SO_G=="G":
        text="""
        ISpAG _ مبارز
        ویژگی ها: خیال‌پرداز، خودانگیخته، خودبیان‌گر و معاشرتی            
        مشاغل: فعال حقوق مدنی، قاصد یا سفیر سیاسی، متخصص زیبایی،
        روزنامه‌نگار، مدیر روابط عمومی، مربی هنر‌های نمایشی، نماینده‌ی اتحادیه
        """
        with open(file_path, "a", encoding="utf-8") as notesave:
            notesave.write(text)        
        labtext.set(text)
    elif mosalat_I_F=="F" and mosalat_SP_D=="D" and mosalat_A_P=="P" and mosalat_SO_G=="G":
        text="""
        FDPG _ تمام‌کننده
        ویژگی ها: واقع‌گرا، خودانگیخته، پذیرا و معاشرتی            
        مشاغل: خدمه‌ی آمبولانس، نیروهای مسلح، صندوق‌دار،
        پرستار، افسر پلیس، نگهبان زندان، آتش‌نشان، محافظ
        """
        with open(file_path, "a", encoding="utf-8") as notesave:
            notesave.write(text)        
        labtext.set(text)  
    elif mosalat_I_F=="F" and mosalat_SP_D=="SP" and mosalat_A_P=="P" and mosalat_SO_G=="G":
        text="""
        FSpPG _ همکار
        ویژگی ها: واقع‌گرا، خودانگیخته، پذیرا و معاشرتی            
        مشاغل: مهمان‌دار هواپیما، متصدی پیش‌خوان در کافی‌شاپ،
        دستیار دندان پزشک، آرایش‌گر مو، کاپیتان تیم، معلم، منشی، کمک مربی ورزشی   
        """
        with open(file_path, "a", encoding="utf-8") as notesave:
            notesave.write(text)        
        labtext.set(text)  
    elif mosalat_I_F=="I" and mosalat_SP_D=="D" and mosalat_A_P=="P" and mosalat_SO_G=="G":
        text="""
        IDPG _ رازدار
        ویژگی ها: خیال‌پرداز، خودانگیخته، پذیرا و معاشرتی            
        مشاغل: کارورز پرستاری، سرپرست، پرستار آسایشگاه بیماری‌های روانی، مربی
        پرستاری، مربی درمان‌گری، فعال اجتماعی، درمان‌گر
        """
        with open(file_path, "a", encoding="utf-8") as notesave:
            notesave.write(text)        
        labtext.set(text)     
    elif mosalat_I_F=="I" and mosalat_SP_D=="SP" and mosalat_A_P=="P" and mosalat_SO_G=="G":
       text="""
        ISpPG _ همکار
        ویژگی ها: خیال‌پرداز، خوداگیخته، پذیرا و معاشرتی            
        مشاغل: مشاور، بازاریاب، پرستار، متصدی پذیرش، خرده
        فروش، کارگر صحنه، مستخدم
        """
       with open(file_path, "a") as notesave:
            notesave.write(text)       
       labtext.set(text)
    elif mosalat_I_F=="F" and mosalat_SP_D=="D" and mosalat_A_P=="A" and mosalat_SO_G=="SO":
        text = """
        FDASo _ ترتیب دهنده
        ویژگی ها: واقع‌گرا، مشرف بر خود، خودبییان‌گر و منزوی            
        مشاغل: وکیل دعاوی، بازرس پلیس، مشاور حقوقی، مسئول
        کارسنجی، مامور گمرک، بارزس مالیات
        """
        with open(file_path, "a", encoding="utf-8") as notesave:
            notesave.write(text)        
        labtext.set(text) 
    elif mosalat_I_F=="F" and mosalat_SP_D=="SP" and mosalat_A_P=="A" and mosalat_SO_G=="SO":
       text="""
        FSpASo _ مشاور
        ویژگی ها: واقع‌گرا، خودانگیخته، خودبیان‌گر و منزوی            
        مشاغل: وارد/صادر کننده، خریدار، کارآفرین، کارگزار کالا،
        مدیر فروش، تاجر، خریدار املاک، مدیر راه‌سازی، مدیر باشگاه
        """
       with open(file_path, "a") as notesave:
            notesave.write(text)       
       labtext.set(text)
    elif mosalat_I_F=="I" and mosalat_SP_D=="D" and mosalat_A_P=="A" and mosalat_SO_G=="SO":
        text="""
        IDASo _ طراح
        ویژگی ها: خیال‌پرداز، مشرف بر خود، خودبیان‌گر و منزوی            
        مشاغل: تحلیل‌گر، معمار، مشاور تجاری، بازرس، روزنامه‌نگار
        ، کتاب‌دار، جامعه‌شناس، دانشمند علوم پزشکی
        """
        with open(file_path, "a", encoding="utf-8") as notesave:
            notesave.write(text)        
        labtext.set(text)
    elif mosalat_I_F=="I" and mosalat_SP_D=="SP" and mosalat_A_P=="A" and mosalat_SO_G=="SO":
       text="""
        ISpASo _ ایده‌آلیست
        ویژگی ها: خیال‌پرداز، خودانگیخته، خودبیان‌گر و منزوی            
        مشاغل: معمار، هنرمند، نویسنده، سرآشپز، مربی ایروبیک،
        طراح داخلی، موسیقی‌دان، مجسمه ساز
        """
       with open(file_path, "a", encoding="utf-8") as notesave:
            notesave.write(text)
       labtext.set(text)
    elif mosalat_I_F=="F" and mosalat_SP_D=="D" and mosalat_A_P=="P" and mosalat_SO_G=="SO":
       text="""
        FDPSo _ محقق
        ویژگی ها: واقع‌گرا، مشرف بر خود، پذیرا و منزوی
        مشاغل: کاردان حسابداری، حسابرس، بایگان، کارشناس بیمه،
        راننده، مهندس، محقق عملیات مدیریتی
        """
       with open(file_path, "a") as notesave:
            notesave.write(text)       
       labtext.set(text)
    elif mosalat_I_F=="F" and mosalat_SP_D=="SP" and mosalat_A_P=="P" and mosalat_SO_G=="SO":
       text="""
        FSpPSo _ اجرا‌کننده
        ویژگی ها: واقع‌گرا، خودانگیخته، پذیرا و منزوی            
        مشاغل: کاردان حسابداری، راهنمای تور، آشپز، متخصص تغذیه، مفسر،
        متخصص کامپیوتر، متخصص فوریت‌های پزشکی، افسر گشت جاده‌ای، جراح
        """
       with open(file_path, "a") as notesave:
            notesave.write(text)       
       labtext.set(text)
    elif mosalat_I_F=="I" and mosalat_SP_D=="D" and mosalat_A_P=="P" and mosalat_SO_G=="SO":
        text="""
        IDPSo _ متخصص
        ویژگی ها: خیال‌پرداز، مشرف بر خود، پذیرا و منزوی            
        مشاغل: کتابدار، نگهبان موزه، کارگر مزرعه، کارگر ساختمانی،
        باغبان، تاریخ‌دان، پیک تحویل کالا، سفال‌گر، چوپان، عایق‌گر، زین‌ساز، اسلحه‌ساز، برنامه‌ریز
        """
        with open(file_path, "a", encoding="utf-8") as notesave:
            notesave.write(text)       
        labtext.set(text)
    elif mosalat_I_F=="I" and mosalat_SP_D=="SP" and mosalat_A_P=="P" and mosalat_SO_G=="SO":
       text="""
        ISpPSo _ سرگردان
        ویژگی ها: خیال‌پرداز، مشرف بر خود، پذیرا و منزوی            
        مشاغل: متصدی پیش‌خوان در کافی‌شاپ، مربی ایروبیک،
        شخصیت رسانه‌ای، مدل، باربر، کارگر خط تولید، فروشنده، مستخدم
        """
       with open(file_path, "a") as notesave:
            notesave.write(text)       
       labtext.set(text)


# function hayi baraye button ha va amaliyat hayeshan
def one():
    global press_btn
    global bool_check
    global num
    global labScore

    num=1
    bool_check=True
    labScore=tk.Label(win,text="1  ",font="calibr 40",bg="#6C5E5E")
    labScore.place(x=560,y=280)
    press_btn.config(text="")
#------------------------------------------------------------------------------------------------------------------------------
def two():
    global press_btn
    global bool_check
    global num

    num=2
    bool_check=True
    labScore=tk.Label(win,text="2  ",font="calibr 40",bg="#6C5E5E")
    labScore.place(x=560,y=280)
    press_btn.config(text="")
#------------------------------------------------------------------------------------------------------------------------------    
def three():
    global press_btn
    global bool_check
    global num
    
    num=3
    bool_check=True
    
    labScore=tk.Label(win,text="3  ",font="calibr 40",bg="#6C5E5E")
    labScore.place(x=560,y=280)
    press_btn.config(text="")
#------------------------------------------------------------------------------------------------------------------------------
def fore():
    global press_btn
    global bool_check
    global num

    num=4
    bool_check=True
    
    labScore=tk.Label(win,text="4  ",font="calibr 40",bg="#6C5E5E")
    labScore.place(x=560,y=280)
    press_btn.config(text="")
#------------------------------------------------------------------------------------------------------------------------------
def five():
    global press_btn
    global bool_check
    global num

    num=5
    bool_check=True
    
    labScore=tk.Label(win,text="5  ",font="calibr 40",bg="#6C5E5E")
    labScore.place(x=560,y=280)
    press_btn.config(text="")
#------------------------------------------------------------------------------------------------------------------------------
def six():
    global press_btn
    global bool_check
    global num

    num=6
    bool_check=True
    
    labScore=tk.Label(win,text="6  ",font="calibr 40",bg="#6C5E5E")
    labScore.place(x=560,y=280)
    press_btn.config(text="")
#------------------------------------------------------------------------------------------------------------------------------
def seven():
    global press_btn
    global bool_check
    global num

    num=7
    bool_check=True
    
    labScore=tk.Label(win,text="7  ",font="calibr 40",bg="#6C5E5E")
    labScore.place(x=560,y=280)
    press_btn.config(text="")
#------------------------------------------------------------------------------------------------------------------------------
def eight():
    global press_btn
    global bool_check
    global num

    num=8
    bool_check=True
    
    labScore=tk.Label(win,text="8  ",font="calibr 40",bg="#6C5E5E")
    labScore.place(x=560,y=280)
    press_btn.config(text="")
#------------------------------------------------------------------------------------------------------------------------------
def nine():
    global press_btn
    global bool_check
    global num
    global labScore


    num=9
    bool_check=True
    
    labScore=tk.Label(win,text=" 9  ",font="calibr 40",bg="#6C5E5E")
    labScore.place(x=560,y=280)
    press_btn.config(text="")
#------------------------------------------------------------------------------------------------------------------------------
def ten():
    global press_btn
    global bool_check
    global num

    num=10
    bool_check=True
    
    labScore=tk.Label(win,text="10",font="calibr 40",bg="#6C5E5E")
    labScore.place(x=560,y=280)
    press_btn.config(text="")

# function button aval (start)
def start():

         


    global press_btn
    global bool_btn_start
    bool_btn_star = True
    btn_save.place(x=10000,y=1)
    if bool_btn_star == True :
        press_btn=tk.Label(win,bg="#6C5E5E",text="press button",font="calibr 40")
        press_btn.place(x=455,y=280)
        
    # Type haye kenar adad 
    global labPT, labPTtext
    labPTtext = tk.StringVar()
    labPT=tk.Label (win,font="Tahoma 55",fg="white",bg="#4D4646", textvariable=labPTtext)
    labPT.place(x=100,y=390)

    labtext.set(sovalat[0])
    labPTtext.set(type_of_sovalat[0])

    btn4=tk.Button(win,text=1,font="Tahoma 30", command=one)
    btn4.place(x=200,y=400)
    btn5=tk.Button(win,text=2,font="Tahoma 30",command=two)
    btn5.place(x=291,y=400)
    btn6=tk.Button(win,text=3,font="Tahoma 30",command=three)
    btn6.place(x=380,y=400)
    btn7=tk.Button(win,text=4,font="Tahoma 30",command=fore)
    btn7.place(x=471,y=400)
    btn8=tk.Button(win,text=5,font="Tahoma 30",command=five)
    btn8.place(x=560,y=400)
    btn9=tk.Button(win,text=6,font="Tahoma 30",command=six)
    btn9.place(x=651,y=400)
    btn10=tk.Button(win,text=7,font="Tahoma 30",command=seven)
    btn10.place(x=740,y=400)
    btn11=tk.Button(win,text=8,font="Tahoma 30",command=eight)
    btn11.place(x=831,y=400)
    btn12=tk.Button(win,text=9,font="Tahoma 30",command=nine)
    btn12.place(x=920,y=400)
    btn13=tk.Button(win,text=10,font="Tahoma 30",command=ten)
    btn13.place(x=1010,y=400)

        
        
        
        
    btn.place(x=500,y=1000)


    #btn bad
    btn3=tk.Button(text=">>",bg="#302929",fg="blue",font="calibri 25",command=next)
    btn3.place(x=600,y=530)
#------------------------------------------------------------------------------------------------------------------------------
# amaliyat haye btn badi
def next():
    global step
    global bool_check
    global num
    global x
    global labScore


    
    
    btn4=tk.Button(win,text=1,font="Tahoma 30", command=one)
    btn4.place(x=200,y=400)
    btn5=tk.Button(win,text=2,font="Tahoma 30",command=two)
    btn5.place(x=291,y=400)
    btn6=tk.Button(win,text=3,font="Tahoma 30",command=three)
    btn6.place(x=380,y=400)
    btn7=tk.Button(win,text=4,font="Tahoma 30",command=fore)
    btn7.place(x=471,y=400)
    btn8=tk.Button(win,text=5,font="Tahoma 30",command=five)
    btn8.place(x=560,y=400)
    btn9=tk.Button(win,text=6,font="Tahoma 30",command=six)
    btn9.place(x=651,y=400)
    btn10=tk.Button(win,text=7,font="Tahoma 30",command=seven)
    btn10.place(x=740,y=400)
    btn11=tk.Button(win,text=8,font="Tahoma 30",command=eight)
    btn11.place(x=831,y=400)
    btn12=tk.Button(win,text=9,font="Tahoma 30",command=nine)
    btn12.place(x=920,y=400)
    btn13=tk.Button(win,text=10,font="Tahoma 30",command=ten)
    btn13.place(x=1010,y=400)
    
    global press_btn
    if bool_check==True:
        labtext.set(sovalat[x])
        labPTtext.set(type_of_sovalat[x])
        answers.append(num)
        x+=1    
        step+=1
        press_btn.config(text="",font="calibr 40")
        press_btn.place(x=455,y=280)
    elif bool_check==False:
        press_btn.config(textvariable="press button",font="calibr 40")
        press_btn.place(x=455,y=280)

    if step==40:
        btn_Computing=tk.Button(text="press me for Computing",bg="#6C5E5E",command=Computing,font="calibr 30")
        btn_Computing.place(x=400,y=520)
def save():
    global name_note_txt
    global btn
    global labtext
    global notesave
    global file_path

    text_age=en_age.get()
    text_family=en_family.get()
    text_name=en_name.get()
    # print(text_family)
    # print(text_name)
    # print(text_age)

    custom_dir = filedialog.askdirectory()
    file_name = "testgir.txt"
    file_path = os.path.join(custom_dir, file_name)
    name_note_txt = text_name + "_"+text_family + "   |  age = "+ text_age
    with open(file_path, "w") as notesave:
        notesave.write(name_note_txt)

    btn=tk.Button(win,text="start",bg="black",fg="yellow",font="calibri 35",command=start)
    btn.place(x=500,y=500)
    en_name.place(x=10000,y=1)
    lab_name.place(x=10000,y=1)
    en_family.place(x=10000,y=1)
    lab_family.place(x=10000,y=1)
    en_age.place(x=10000,y=1)
    lab_age.place(x=10000,y=1)
    
global labtext
labtext = tk.StringVar()
labtext.set("""در این ازمون باید به عبارت های داده شده دقت کنید
         و بر اساس میزانی که ان عبرت در مورد شما صدق میکند
         نمره ای از یک تا ده به خود بدهید اگر مثلا در عبا   رتی
         نمره یک به خود بدهید یعنی اینکه آن عبارت اصلا در 
         مورد شما صدق نمیکند از طرف دیگر نمره ده به معنای 
         این است که عبارت مورد نظر کاملا در مورد شما صدق میکند
         نمره پنج یا شش یعنی عبارت در مورد شما صدق میکند
         و گاهی نمیکند هر چه این نمره بیشتر باشد یعنی که عبارت
         بیشتر به واقعیت شخصیت شما نزدیک است""")
lab=tk.Label(win,width=90,height=10,font="Tahoma 20",textvariable=labtext,bg="#6C5E5E",justify="right")
lab.pack(pady=20)

text_age=""
text_family=""
text_name=""
# vorodi safhe aval
lab_name=tk.Label(text="نام خود را وارد کنید :",font="Tahoma 19")
lab_name.place(x=50,y=400)
en_name=tk.Entry(font="Tahoma 19",width=15,textvariable=text_name)
en_name.place(x=280,y=400)

lab_family=tk.Label(text=" نام خانوادگی خود را وارد کنید :",font="Tahoma 19")
lab_family.place(x=550,y=400)
en_family=tk.Entry(font="Tahoma 19",width=15,textvariable=text_family)
en_family.place(x=900,y=400)


lab_age=tk.Label(text="سن خود را وارد کنید :",font="Tahoma 19")
lab_age.place(x=300,y=450)
en_age=tk.Entry(font="Tahoma 19",width=15,textvariable=text_age)
en_age.place(x=550,y=450)

bool_btn_start = False

press_btn=tk.Label(win,bg="#6C5E5E",text="",font="calibr 40")
press_btn.place(x=455,y=280)

bool_btn_start = False
btn_save=tk.Button(text="save",font="calibri 35",command=save)
btn_save.place(x=500,y=500)
win.mainloop()
