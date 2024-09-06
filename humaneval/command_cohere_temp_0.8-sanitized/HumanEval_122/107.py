def add_elements(arr, k):
    sum_two_digits = sum(el for el in arr[:k] if len(str(el)) <= 2)
    return sum_two_digits
    # The line above uses a generator expression to create a sum of all elements in the array arr[:k] that have length less than or equal to 2. The resulting generator is then passed to the sum function which calculates the total sum of these values.