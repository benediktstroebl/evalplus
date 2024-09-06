def choose_num(x, y):
    max_even = -1
    temp_num = y
    while temp_num >= x:
        if temp_num % 2 == 0:
            max_even = temp_num
        temp_num -= 1
    return max_even if max_even != -1 else -1