site={"user":
    {"login":"user0",
      "password":"12345"}
}
answer=input("Додати нового користувача? 1 - так 0 - ні")
while answer!="0":
    login=input("Введи логін  ")
    password=input("Введи пароль  ")
    site[login]={"login":login, "assword":password}
    answer=input("Додати нового користувача? 1 - так 0 - ні")
print("Cписок логінів, зареєстрованих на сайті")
for user in site:
    print(user)
q1=input("Введи логін ") 
if q1 in site:
    print(site[q1])
else:
    print("Такого користувача немає") 
