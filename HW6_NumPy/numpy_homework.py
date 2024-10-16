import os
os.system("cls")
import numpy as np


def bai1():
    x = np.array([x for x in range(1,11)])
    print("a) Kiểm tra kiểu dữ liệu của các phần tử trong mảng")
    print(type(x))
    print("b) Kiểm tra kích thước của mảng(trả về một tuple dạng(n,))")
    print(x.shape)
    print("c) Tính mảng y và z sao cho y[i] = pi/2 - x[i] và z[i] = cos(x[i]) - sin(x[i])")
    y = np.pi/2 - x
    z = np.cos(x) - np.sin(x)
    print("Y=", y)
    print("Z=", z)
    print("d) Tìm những số chẵn/lẻ/số nguyên tố trong mảng.")
    bool_idx = (x%2==0)
    print(x[bool_idx])
    print("e) Thay thế các số chẵn trong mảng bằng -1, các số lẽ trong mảng bằng -2")
    t = np.where(bool_idx, -1, -2)
    print(t)

def bai2():
    x = np.arange(10)
    print(np.max(x)) #return max
    print(np.min(x)) #return min
    print(np.argmax(x)) #return index of max
    print(np.argmin(x)) #return index of min

def bai3():
    a = np.array([1,2,3,2,3,4,3,4,5,6])
    b = np.array([7,2,10,2,7,4,9,4,9,8])
    print("Tìm các phần tử xuất hiện ở cả hai mảng. Ví dụ kết quả là : array([2, 4])")
    print("a) Dùng hàm np.intersect1d()")
    # np.intersect1d(a,b) trả về một mảng chứa các phần tử xuất hiện trong cả hai mảng a và b.
    print(np.intersect1d(a,b))
    print("b) Không sử dụng hàm trên")
    print(np.unique([x for x in a if x in b]))

def bai4():
    a = np.array([2, 6, 1, 9, 10, 3, 27])
    bool = (a>5) & (a<10)
    print(a[bool])
    
def bai1_B():
    n = 10
    arr = np.ones((n,n))
    arr[1:-1,1:-1] = 0
    print(arr)

def bai2_B():
    arr = np.arange(15).reshape(3,5)
    print(arr)
    print("a) Tính tổng mỗi dòng, tổng mỗi cột.")
    print(arr.sum(axis=1)) #axis = 1 -> dòng
    print(arr.sum(axis=0)) #axis = 0 -> cột
    print("b) Tìm giá trị lớn nhất/nhỏ nhất mỗi dòng/mỗi cột.")
    print(arr.max(axis=1))
    print(arr.max(axis=0))
    print(arr.min(axis=1))
    print(arr.min(axis=0))
    print("c) Tìm những số chẵn/lẻ trong ma trận.")
    print(arr[arr%2==0])
    print(arr[arr%2!=0])
    print("d) Tính trung bình cộng các cột có chỉ số chẵn (0,2,4)")
    print(arr[:, ::2].mean(axis=0))#arr[:, ::2] chọn các cột có chỉ số chẵn (bắt đầu từ 0, bước nhảy là 2).
    print("e) Tính tổng các phần tử có hai chỉ số đều là số chẵn.")
    print(arr[::2,::2].mean())
    print("f) Tính khoảng cách giữa giá trị nhỏ nhất và lớn nhất trên mỗi dòng.")
    print(arr.max(axis=1)-arr.min(axis=1))

def bai3_B():
    arr = np.arange(25).reshape(5,5)
    arr = arr + 2
    print(arr[:,:])
    print("Tính tổng các phần tử trên đường chéo chính/phụ.")
    print(np.sum(np.diag(arr))) 
    print(np.sum(np.diag(arr[::-1]))) 

    print("Tìm giá trị lớn nhất/nhỏ nhất trên đường chéo chính/phụ")
    print(np.max(np.diag(arr))) # diag(arr) -> lấy giá trị đường chéo chính
    print(np.max(np.diag(arr[::-1]))) # diag(arr[::-1]) -> lấy giá trị đường chéo phụ

if __name__ == "__main__":
    # bai1()
    # bai2()
    # bai3()
    # bai4()
    # bai1_B()
    # bai2_B()
    bai3_B()