def is_square_number(n): # so chinh phuong
    if n < 0:
        return False
    for i in range(int(n**0.5) + 1):
        if i*i == n:
            return True
    return False

def is_perfect_number(n): # so hoan hao
    if n < 0:
        return False
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def is_symmetric_number(n): # so doi xung
    if n < 0:
        return False
    str_n = str(n)
    return str_n == str_n[::-1]


def is_prime(n): # so nguyen to
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True
    
def main():
    n = int(input("Nhap n: "))
    if is_square_number(n):
        print(n, "la so chinh phuong")
    else:
        print(n, "khong la so chinh phuong")
    if is_perfect_number(n):
        print(n, "la so hoan hao")
    else:
        print(n, "khong la so hoan hao")
    if is_symmetric_number(n):
        print(n, "la so doi xung")
    else:
        print(n, "khong la so doi xung")
    if is_prime(n):
        print(n, "la so nguyen to") 
    else:
        print(n, "khong la so nguyen to")

def bai4():
    m = int(input("Nhap m: "))
    for i in range(1, m+1):
        if is_prime(i):
            print(i, end=" ")



if __name__ == "__main__":
    # main()
    bai4()
