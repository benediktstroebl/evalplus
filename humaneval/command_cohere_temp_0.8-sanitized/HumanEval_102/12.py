def choose_num(x, y):
    max_even = -1
    target = y
    while target > x:
        if target % 2 == 0 and target not in (x, y):
            max_even = target
        target -= 2
    return max_even