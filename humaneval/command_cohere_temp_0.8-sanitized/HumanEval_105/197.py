def by_length(arr):
    sorted_arr = sorted(arr)
    sorted_arr = sorted_arr[::-1]
    res = []
    for num in sorted_arr:
        if 1 <= num <= 9:
            res.append(str(num)[0] + "een")
    return res if res else []