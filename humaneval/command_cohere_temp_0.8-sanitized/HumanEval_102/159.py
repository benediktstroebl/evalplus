def choose_num(x, y):
    max_even = -1
    try:
        max_even = max(x, y, key=lambda n: (-n % 2, n))
    except ValueError:
        pass
    return max_even