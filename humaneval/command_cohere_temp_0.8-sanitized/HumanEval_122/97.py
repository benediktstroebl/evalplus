def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i]))<=2:
            sum_two_digits += arr[i]
    return sum_two_digits