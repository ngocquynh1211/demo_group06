a = int(input("nhap so thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

if a > b and a > c:
    print(f"số lớn nhất là {a}")
elif b > a and b > c:
    print(f"Số lớn là {b}")
else:
    print(f"số lớn nhất là {c}")
