import time

# Giriş Ekranı
username = input("Kullanıcı adınızı belirleyiniz: ")
password = input("Şifrenizi belirleyiniz: ")

print("Kodlama.io sitesine kaydınızı tamamladınız.")
giris_onayi = input("Sisteme giriş yapmak istiyor musunuz? E = evet / H = hayır : ")
if giris_onayi == "E":
  login_username = input("Kullanıcı adınızı giriniz: ")
  login_password = input("Şifrenizi giriniz: ")
  if (login_username == username) and (login_password == password):
    print("Sisteme giriş yapılıyor...")
    time.sleep(1)
    print("Sisteme giriş yapıldı.")
  else:
    print("Kullanıcı adı veya şifreniz hatalı. Lütfen tekrar deneyin.")
elif giris_onayi == "H":
  print("Giriş ekranından çıkılıyor.")


# Kursların listelenmesi ve fonksiyon kullanımı
def course_take(all_courses):
  my_courses = []
  for this_course in all_courses:
    take_course = input(this_course + " kursunu almak istiyorsanız evet anlamına gelen 'E' harfini giriniz. Almak istemiyorsanız başka herhangi bir harf giriniz: ")
    if take_course == "E":
      my_courses.append(this_course)

  print("Tüm kurslarınız listeleniyor...")
  time.sleep(1)
  print("Tüm Kurslarınız: ")
  for that_course in my_courses:
    print(that_course)

# Fonksiyonun çağrılması
all_courses = ["Python Giriş",
               "Python Orta Düzey",
               "Python İleri Düzey",
               "Python Gerçek Hayat Uygulamaları",
               "Python ve Etik Hacking"]
course_take(all_courses)
