def choose_num(x, y):
    max_even = max(x, y) if (x == y) or (x % 2 == y % 2) else -1
    return max_even if max_even >= x and max_even <= y else -1