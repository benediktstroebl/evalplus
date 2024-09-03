def maximum(arr, k):
    arr = list(map(int, arr))  # Convert array to list of integers
    if k <= len(arr):
        return arr[:k]
    else:
        raise ValueError("k is greater than the length of the array")
arr = [-3, -4, 5]
k = 3