def add_elements(arr, k):
    sum_two_digits = sum(ele for ele in arr[:k] if len(str(ele)) <= 2)
    return sum_two_digits
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]