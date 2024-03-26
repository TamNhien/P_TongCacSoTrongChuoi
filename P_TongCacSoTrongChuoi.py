string = input("Nhập chuỗi: ")
total = sum(int(char) for char in string if char.isdigit())
print("Tổng các số trong chuỗi là : ", total)

