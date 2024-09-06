def choose_num(x, y):
    max_even = (x + y) // 2
    max_even += max_even % 2
    if max_even >= x and max_even <= y:
        return max_even
    elif max_even > y:
        return -1
    elif max_even < x:
        return -1