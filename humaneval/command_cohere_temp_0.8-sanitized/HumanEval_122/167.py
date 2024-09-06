def add_elements(arr, k):
    sum_two_digits = sum(ele for ele in arr[:k] if len(str(ele)) <= 2)
    return sum_two_digits
    # The line above uses a generator expression to create a sequence of integers from the first k elements of arr, and then sums them if their string representation has at most two digits (which corresponds to integers with values less than or equal to 99).