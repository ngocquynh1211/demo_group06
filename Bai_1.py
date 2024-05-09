# Bài 1: Viết chương trình nhập vào chiều dài và chiều rộng của hình chữ nhật và cho biết đó có phải là hình vuông hay không.

x = int(input("Nhập chiều rộng: "))
y = int(input("Nhập chiều dài: "))

if x == y:
    print("đây là hinh vuông")
else:
    print("Không phải là hình vuông")