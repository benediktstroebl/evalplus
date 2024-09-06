def choose_num(x, y):
    max_even = max(x, y)
    min_even = min(x, y)
    if max_even - min_even % 2 == 0 and max_even >= min_even:
        return max_even
    else:
        return -1