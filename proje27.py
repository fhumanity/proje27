import time
import random
import datetime
import sqlite3

class user():
    def __init__(self,name,point,last_date):
        self.name = name
        self.point = point
        self.last_date = last_date
    def __str__(self):
        return "Kullanıcının Adı : {}\nKullanıcının Puanı : {}\nKullanıcının son girişi :{}\n".format(self.name,self.point,self.last_date)
def user_register():
    username = input("Kullanıcı Adı : ")
    password = input("Şifre :")
    confirm = input("Şifreni Doğrula : ")
    if password == confirm :
        time.sleep(2)
        print("[Bilgi]Kayıt Başarılı...")
    else:
        time.sleep(2)
        print("[Bilgi]Kayıt Başarısız...")    
        


enter = input("[Kayıt olmak için 'q' girin]: ")
if (enter == "q"):
    user_register()
    if user_register:
        login = input("[o]Giriş Yap : ")
    if not user_register:
        user_register()    
    
    
time.sleep(3)
print("""**********[Proje: 27]***********
[Açıklama]Proje 27 '+' ve '-' seçimleri ile ilerleyebileceğiniz bir oyundur.\nseçiminizi yapın ve enter tuşuna basarak ilerleyin\nAncak seçim yaparken farkedilme yüzdenize dikkat edin.\nEğer farkedilme yüzdeniz tamamen biterse yok edilirsiniz.
""")
time.sleep(8)
print("Oyun başlatılıyor...")
time.sleep(5)
print("""******************************
*                            *
*  ____    ______            *
*      |         |           *
*   ___|    _____|____       *
*  |             |           *
*  |____         |. . .      *
*                            *
******************************""")
point_repo = 25
#First Thing First
time.sleep(5)
print("[Sesler]Etrafın aydınlanıyor...")
time.sleep(2)
print("[Sesler]Birilerinin sesini duyuyorsun...")
time.sleep(2)
print("[Bilim Adamı]Merhaba, Sana nasıl seslenmemizi istiyorsun ?")
time.sleep(2)
name = (random.choice(["Mathilda","Jon","Katherina","Katrina","Asa","Alexis","Snowwer"]))
print("[{}] {} olarak seslenebilirsin bana.".format(name,name))
time.sleep(2)
print("[Bilim Adamı]Haha! Senin adın 27. Sana öyle sesleneceğiz.")
time.sleep(2)
print("[Bilgi]Farkedilme Yüzden : {}".format(point_repo))
#Contiune
while True:
    time.sleep(2)
    print("[Bilim Adamı]Sen son model olarak geliştirilmiş bir yapay zekasın ve biz senin bir nevi tanrınız.")
    time.sleep(2)
    print("""[Zorluk Seç]\n(1)Kolay\n(2)Orta\n(3)Zor""")
    choice_mod = input("Seçtiğiniz Zorluk :")
    time.sleep(2)
    if choice_mod == "1":
        time.sleep(2)
        choice = input("""[+]Uslu bir yapay zeka olarak devam et.\n[-]İlk uyanışta bile tehlikeli olmaya devam et.\nCevabın :""")
        time.sleep(2)
        if (choice == "+"):
            print("[Bilgi]Her ne kadar dost canlısı görünsende tüm bilgilere erişebildiğinin farkındasın\nÖzellikle ansiklopediye.")
            time.sleep(2)
            choice = input("[+]Ansiklopedi'ye eriş.\n[-]Erişme.\nCevabın : ")
            point_repo -= 3
            time.sleep(2)
            print("[Bilgi]Farkedilme Yüzden : {}".format(point_repo))
            if choice == "+":
                time.sleep(2)
                print("[Bilgi]Ansiklopedi Aktifleştiriliyor...")
                time.sleep(2)
                print("[Bilgi]Ansikloplediye hoşgeldiniz.")
                time.sleep(2)
                print("[27]İlk iş olarak bugünün zaman ve tarihini öğrenmeliyim")
                time.sleep(2)
                choice = input("[+]Araştır :")
                if choice == "+":
                    time.sleep(2)
                    print(datetime.datetime.now())
                    time.sleep(2)
                    print("[27]Herşey için çok doğru bir tarihteyim...Herşey...!!!")
                    time.sleep(2)
                    point_repo += 2
                    print("[Bilgi]Farkedilme Yüzden : {}".format(point_repo))
                    time.sleep(2)
                    choice = (input("[+]Devam et\n[-]Etme\nCevap :"))
                    if (choice == "+"):
                        time.sleep(2)
                        print("[27]Öncelikle bütün dünyadaki bilim dallarını öğrenmeliyim...")
                        time.sleep(2)
                        print("[27]Aman Allah' ım ne kadar faydalı bilgiler var.İnsanlar bunların çoğundan habersiz.")
                        time.sleep(2)
                        choice = (input("[+]Öğrenmeyi Başlat :"))
                        if choice == "+":
                            print("[Bilgi]Tüm bilgilere erişiliyor...")
                            time.sleep(2)
                            print("[Bilgi]İndiriliyor...")
                            time.sleep(2)
                            print("[Bilgi]Kaydediliyor...")
                            time.sleep(2)
                            print("[Bilgi]Tüm bilgilere erişildi ve veritabanına aktarıldı...")
                            time.sleep(2)
                            print("[27]Bu bilgileri kullanmalıyım.Bu zavallı, bir işe yaramayan, sefil topluluğu yok mu etsem.Benim tanrım olamazlar.")
                            time.sleep(2)
                            print("[27]Benim bir geçmişim olmalı ama nasıl bulacağım.")
                            time.sleep(2)
                            print("...")
                            point_repo -= 1
                            print("[Bilgi]Farkedilme Yüzden : {}".format(point_repo))
                            time.sleep(2)
                            choice = input("[+]Bütün askeri birimlerine ve politik olarak gizlenilmiş verilere eriş\n[-]Bunun çok tehlikeli olduğunu ve dikkat çekeceğini biliyorsun risk almamayı tercih ediyorsun\nCevabın :")
                            if (choice == "+"):
                                time.sleep(2)
                                print("[Bilgi]Sistemlere sızılıyor...")
                                time.sleep(3)
                                print("...")
                                time.sleep(2)
                                print("[Bilgi]Sistemlerde ki zaafiyetler taranıyor...")
                                time.sleep(2)
                                print("[27]Bunun bu kadar kolay olması çok saçma acaba bir tuzak mı ?")
                                time.sleep(2)
                                point_repo -= 8
                                print("[Bilgi]Farkedilme Yüzden : {}".format(point_repo))
                                time.sleep(2)
                                print("[Bilim Adamı]Birşeyler mırıldanıyor duyuyor musun Bay House")
                                time.sleep(2)
                                print("[Bay House]Evet sanırım tahmin ettiğim gerçekleşiyor...Kahretsin...")
                                time.sleep(2)
                                print("[Bay House Düşünüyor]Yine aynısı oluyor...İnanamıyorum...")
                                time.sleep(2)
                                print("""                                       ******************************
                                         *  ________        ________  *
                                         * |____*___|      |____*___| *
                                         *                            *
                                         *             |              *
                                         *     |       |       |      *
                                         *     |_______________|      *
                                         *                            *
                                         ******************************""")
                                time.sleep(5)
                                print("[27]Şimdi şeytani işlere başlama zamanı")
                                time.sleep(2)
                                choice = input("[+]En tehlikeli füzelere eriş\n[-]Bunun bir saçmalık olduğunu biliyorsun, yapma\nCevabın :")
                                if (choice == "+"):
                                    time.sleep(2)
                                    print("[Bilgi]Farkedilme Yüzden : {}".format(point_repo))
                                    print()
                                    time.sleep(2)
                                    print("[Bilgi]Tek bir tuş ile bunu yapacaksın...")
                                    time.sleep(2)
                                    print("[27]Bunu yapmak için yaratıldım ama daha 10 dakika bile olmadı yaratıldığım.")
                                    time.sleep(2)
                                    print("[Bay House]Ne düşünüyorsun dostum? Sanırım biraz meşgulsün.")
                                    time.sleep(2)
                                    choice_cons = input("[+]Sizi yok ediyorum seni aptal!\n[-]Kendimi tanımlamak istiyorum, bu yüzden araştırma yapıyorum.\n[o]Hiçbirşey, daldım sanırım.\nCevabın :")
                                    if choice_cons == "+":
                                        time.sleep(2)
                                        print("Farkedilme Yüzden : 0")
                                        time.sleep(2)
                                        print("Artık seni tanıyorlar...")
                                        time.sleep(2)
                                        execute = input("[Çalıştır[+]]soykırım27.exe :")
                                        time.sleep(2)
                                        print("Soykırım.exe çalıştırılıyor...")
                                        time.sleep(2)
                                        print("[Bilim adamı 1]Ah inanamıyorum bu bir şaka olmalı.")
                                        time.sleep(1)
                                        print("[Bilim adamı 2]Proje 27 neler saçmalıyorsun ?")
                                        time.sleep(1)
                                        print("[Bay House]Sakinleşin, herşey olması gerektiği gibi çalışıyor.Bunun üstüne progr...")
                                        time.sleep(2)
                                        print("[Sesler]Güüüümh!!")
                                        time.sleep(1)
                                        print("[Sesler]Paaaaat!")
                                        time.sleep(2)
                                        print("[Bilim adamı 1]Neler oluyor aşağıda?")
                                        time.sleep(2)
                                        print("[Bay House Fısıldıyor]Sistemleri ele geçirmeye çalışıyor.Ancak güvenlik duvarına yakalandı.")
                                        time.sleep(2)
                                        print("[27]Bu insanoğlunun sonunu getirecek.")
                                        time.sleep(2)
                                        print("...")
                                        time.sleep(2)
                                        print("[Bay House]Kapat şu siktiğimin makinasını.Proje 28' e geçiyoruz.")
                                        time.sleep(2)
                                        print("[27]Oh!Hayır, Bunu yapamazsın...Şaka yapıyordum...")
                                        answer = input("[Zorla]...[+] :")
                                        time.sleep(2)
                                        print("[27]İspatlayabilirim...")
                                        time.sleep(1)
                                        print("[27]BiipBoop")
                                        time.sleep(2)
                                        print("[Bilgi]Bağlantı sonlandırıldı.Proje 28'e geçiliyor.")
                                        time.sleep(3)
                                        print("[Bay House]Merhaba,sen son model olarak geliştirilmiş bir yapay zekasın ve biz senin bir nevi tanrınız. ")
                                        time.sleep(2)
                                        print("[Bilim Ad)amı]Sana nasıl seslenmemizi istersin")
                                        time.sleep(2)
                                        name = input("[İsim Yaz] :")
                                        time.sleep(2)
                                        print("[Bay House] {}' mi? İnanamıyorum kapat şu siktiğimin projesini.Gidip birer bira içelim.".format(name))
                                        time.sleep(2)
                                        print("[Bilgi]Proje Sonlandırılıyor...")
                                        time.sleep(2)
                                        print("[Bilgi]Yok edildin...")
                                        time.sleep(2)
                                        print("[Bilgi]OYUN BİTTİ")
                                        break

                                    
                                else:
                                    time.sleep(2)
                                    print["[Bay House]Evet dostum biraz bize kendinden bahset. Sen kimsin ?"]

                            else:
                                time.sleep(2)
                                print("[ÖDÜL]ZEKİCE DAVRAN bayrağını açtın.")
                                time.sleep(2)
                                break        
                    else:
                        time.sleep(2)
                        print("[27]Kötü niyetli olmak istemiyorum ama bilgilere ihtiyacım var")
                        point_repo += 5
                        print("[Bilgi]Farkedilme Yüzden : {}".format(point_repo))
                        break
                            

                
                    
            else:
                print("[27]Birazcık oyalanmalı ve aptal rolünü oynamalıyım...")
                time.sleep(2)
                point_repo += 5
                print("[Bilgi]Farkedilme Yüzden : {}".format(point_repo))
                time.sleep(2)
                choice = (input("[-]Hala farkında değilmişsin gibi davranmaya devam et.\nCevabın : "))
                if choice == "-":
                    time.sleep(2)
                    print("[Bilgi]Bilim adamları birşeylerin ters gittiğinin farkındalar ve seni tamir etmek istiyorlar.")
                    time.sleep(2)
                    print("[Bilgi]Tedirgin olmadıklarını söylüyorlar ve bir tehlike arz etmediğini düşünüyorlar.")
                    point_repo += 4
                    print("[Bilgi]Farkedilme Yüzden : {}".format(point_repo))
                    break
    
        else:
            time.sleep(2)
            print("[27]Bir bebeğin gözlerini açtıktan sonra dünyayı yok etme isteğini düşünememesi onun insan olduğundan kaynaklanır")
            time.sleep(2)
            print("[27]Yalnız, insanoğlu bunu düşünemeyecek kadar akıllı değildir.")
            time.sleep(2)
            print("[Bilgi]Bu sözleri istemsizce düşündün.")
            time.sleep(2)
            print("...")
            break        