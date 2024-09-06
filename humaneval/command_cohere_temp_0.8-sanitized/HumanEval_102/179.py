def choose_num(x, y):
    max_even = -1
    i = x
    while i <= y:
        if i % 2 == 0:
            max_even = i
        i += 1
    return max_even