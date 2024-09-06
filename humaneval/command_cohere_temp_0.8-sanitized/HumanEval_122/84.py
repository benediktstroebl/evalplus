def add_elements(arr, k):
    sum_two_digits = sum(int(d) for d in arr[:k] if len(str(d)) <= 2)
    return sum_two_digits
    # The above code can be rewritten as follows:
    # return sum(int(d) for d in arr[:k] if len(str(d)) <= 2)