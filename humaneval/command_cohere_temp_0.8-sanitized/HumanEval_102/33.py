def choose_num(x, y):
    max_even = (x + y) // 2
    max_even += max_even % 2
    if max_even in range(x, y + 1):
        return max_even
    else:
        return -1