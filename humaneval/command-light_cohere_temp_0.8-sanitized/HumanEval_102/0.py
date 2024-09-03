def choose_num(x, y):
    if x > y:
        return x
    if x < y or y < 0:
        return -1
    return y