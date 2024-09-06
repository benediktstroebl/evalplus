def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2

    if max_even >= min_even and max_even % 2 == 0:
        return max_even
    elif max_even < min_even or max_even % 2 != 0:
        return -1
    else:
        return -1