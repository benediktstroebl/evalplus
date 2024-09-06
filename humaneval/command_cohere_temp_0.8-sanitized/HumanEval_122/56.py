def add_elements(arr, k):
    sum_two_digits = sum(el for el in arr[:k] if len(str(el)) <= 2)
    return sum_two_digits
    # The line above uses a generator expression to sum only the elements that have at most two digits.