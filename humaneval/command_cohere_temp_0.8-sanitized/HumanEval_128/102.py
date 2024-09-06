def prod_signs(arr):
    result = None
    if arr:
        arr_len = len(arr)
        signs = [arr[i]/abs(arr[i]) for i in range(arr_len)]
        result = sum(abs(num) for num in arr) * prod(signs)
    return result