def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k): 
        num = arr[i]
        if len(str(num))<=2: 
            sum_two_digits += num  
    return sum_two_digits
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4