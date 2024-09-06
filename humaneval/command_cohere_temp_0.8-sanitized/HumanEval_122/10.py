def add_elements(arr, k):
    sum_two_digits = sum(int(d) for d in map(str, arr) if len(d) <= 2)
    return sum_two_digits // k if k != 1 else sum_two_digits
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4