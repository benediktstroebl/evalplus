def choose_num(x, y):
    max_even = max(x, y)
    min_even = min(x, y)
    if max_even - min_even % 2 == 0:
        return -1
    else:
        return max_even