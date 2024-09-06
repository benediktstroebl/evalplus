def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    return max(max_even, min_even) if max_even >= min_even and max_even % 2 == 0 else -1