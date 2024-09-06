def choose_num(x, y):
    max_even = max(x, y)
    floor_odd = max_even - 1
    if (floor_odd % 2 == 0):
        return -1
    else:
        return floor_odd