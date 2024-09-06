def choose_num(x, y):
    max_even = (x + y) // 2
    max_even = max(max_even, x)
    max_even = max(max_even, y)
    return max_even if max_even % 2 == 0 and max_even in range(x, y + 1) else -1