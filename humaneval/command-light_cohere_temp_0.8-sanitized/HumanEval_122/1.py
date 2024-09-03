def add_elements(arr, k):
    n = len(arr)
    if k > n or k < 0:
        raise ValueError("k is out of bounds")
    if k == 0 or k == n:
        return 0

    # Sort the first k elements of the array in ascending order
    arr = arr[:k] + arr[k:]

    return sum(int(x) for x in arr)