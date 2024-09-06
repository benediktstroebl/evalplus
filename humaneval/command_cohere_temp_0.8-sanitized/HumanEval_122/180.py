def add_elements(arr, k):
    sum_two_digits = sum(int(x) for x in arr[:k] if len(str(x)) <= 2)
    return sum_two_digits