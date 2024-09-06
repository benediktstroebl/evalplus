def choose_num(x, y):
    max_even = max((z for z in range(x, y+1) if z % 2 == 0), default=-1)
    return max_even