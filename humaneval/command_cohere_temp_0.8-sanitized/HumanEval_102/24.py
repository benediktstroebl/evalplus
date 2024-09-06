def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    if max_even == min_even or max_even + 1 == min_even:
        return -1
    else:
        return max_even