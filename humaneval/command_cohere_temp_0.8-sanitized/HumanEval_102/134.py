def choose_num(x, y):
    max_even = max(x, y) if (x == y) or ((x + y) & 1) else y
    return max_even if max_even <= max(x, y) else -1