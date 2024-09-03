def add_elements(arr, k):
    # Your implementation here
    return sum(x for x in arr[:k] if len(str(x)) <= 2)
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4