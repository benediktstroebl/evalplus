def by_length(arr):
    sorted_arr = sorted(arr)
    sorted_arr = sorted_arr[::-1]
    res = []
    for n in sorted_arr:
        if 1 <= n <= 9:
            res.append(str(n))
    return res
arr = [2, 1, 1, 4, 5, 8, 2, 3]