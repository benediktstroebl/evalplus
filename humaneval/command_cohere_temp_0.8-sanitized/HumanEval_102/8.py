def choose_num(x, y):
    max_even = max(x, y)
    floor_odd = max(x, y) // 2

    if max_even == floor_odd:
        return max_even
    elif max_even < floor_odd:
        return -1
    else:
        return max_even + 1