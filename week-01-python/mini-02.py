# 미니과제-02-클래스 만들어 보기
class school:
    name = "Eccleston"
    founded = "1957"
    address = "Av.Carabobo56-CABA-Argentina"

school1 = school()
print(school1.name)
print(school1.founded)
print(school1.address)
school3 = school()
school3.name = "San Isidro"
print(school3.name)
print(school1.name)

##### Article class inheritance 상속 응용하기
class afterschool(school):
    hobby = "paddle"

afterschool = afterschool()
print(afterschool.name)
print(afterschool.founded)
print(afterschool.address)
print(afterschool.hobby)
