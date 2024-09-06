def choose_num(x, y):
    max_even = -1
    try:
        max_even = max(x, y, key=lambda z: z if z % 2 == 0 else float('-inf'))
    except ValueError:
        pass
    return max_even