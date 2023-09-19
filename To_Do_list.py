#To-Do List Uygulaması: Bu proje, kullanıcının yapması gereken görevleri ve süreleri ekleyebileceği,
# silip güncelleyebileceği bir to-do list uygulamasıdır. Kullanıcılar ayrıca tamamlanan görevleri de işaretleyebilirler.


#Boş bir to-do-list ve completed_tasks oluştur
to_do_list= []                #görev listesi için
completed_tasks=[]            #tamamlanan görevleri takip etmek için

#seçilen görevi işaretleyen fonksiyon

def task_mark(do_do_list,completed_tasks):
    task = input("işaretlemek istediğiniz görevi girin:")
    if task in to_do_list:
        completed_tasks.append(task)
        to_do_list.remove(task)
        print("görev işaretlendi")
    else:
        print("görev bulunamadı")


#fonksiyon oluşturuyoruz (girdileri alıp listeye ekleyen)

def add_task(to_do_list):
    task=input("Yapılacak görevi girin:")
    to_do_list.append(task)                #listeye görevi ekle
    print("Görev başarıyla eklendi...")

#listedeki görevleri gösteren fonksiyon

def show_tasks(to_do_list,completed_tasks):
    print("Yapılacak görevler:")
    for task in to_do_list:
        print("-"+ task)
    print("işaretlenen görevler:")
    for task in completed_tasks:
        print("-"+task)



#listeden görev silen fonksiyon
def delete_tasks(to_do_list):
    task = input("Silmek istediğiniz görevi girin:")
    if task in to_do_list:
       to_do_list.remove(task)
       print("Başarıyla silindi...")
    else:
        print("Görev bulunamadı")

#görevlere süre koyma

def gorev_suresi(to_do_list):
    task=input("Süre koymak istediğiniz görevi seçiniz:")
    zaman=input("Süreyi gir !!!yazıyla girilecektir rakam olmayacak!!!:")
    if task in to_do_list:
        print("{} görevi {} bitecektir".format(task,zaman))
    else:
        print("...")

#Ana Döngü
while True:
    print('''to_do_list uygulaması
              1. = görev ekle
              2. = görevleri göster
              3. = görev sil
              4. = görevi işaretle
              5. = süre belirle
              6.= çıkış ''')
    choice=input("seçiniz=1/2/3/4")

    if choice=="1":
        add_task(to_do_list)
    elif choice == "2":
        show_tasks(to_do_list,completed_tasks)
    elif choice == "3":
        delete_tasks(to_do_list)
    elif choice == "4":
        task_mark(to_do_list,completed_tasks)
    elif choice =="5":
        gorev_suresi(to_do_list)
    elif choice == "6":
        print("Program sonlanıyor")
        break
    else:
        print("geçersiz islemm!!!!")





