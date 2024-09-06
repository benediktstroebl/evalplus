def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2

    if max_even == min_even or max_even % 2 == 0:
        return max_even
    else:
        return -1