def add_elements(arr, k):
    sum_two_digits = sum(el for el in arr[:k] if len(str(el)) <= 2)
    return sum_two_digits
    # The line above uses a generator expression to create a sum of all elements in the list arr[:k] that have a length of the string representation of less or equal to 2. The resulting generator is then summed up using the sum function.