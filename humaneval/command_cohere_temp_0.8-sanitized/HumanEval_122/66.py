def add_elements(arr, k):
    sum_two_digits = sum(el for el in arr[:k] if len(str(el)) <= 2)
    return sum_two_digits
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4