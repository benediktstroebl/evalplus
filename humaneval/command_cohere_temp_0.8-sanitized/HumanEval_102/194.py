def choose_num(x, y):
    max_even = max(x, y)
    floor_even = max_even - 1
    if floor_even % 2 == 0:
        return max_even
    elif floor_even // 2 < x or floor_even // 2 > y:
        return -1
    else: 
        return floor_even