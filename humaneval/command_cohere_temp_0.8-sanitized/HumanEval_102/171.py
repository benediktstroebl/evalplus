def choose_num(x, y):
    max_even = max(x, y) if (x == y) or ((x + y) & 1) else -1
    return max_even