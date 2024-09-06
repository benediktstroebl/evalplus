def choose_num(x, y):
    max_even = -1
    temp = x
    while temp <= y:
        if temp % 2 == 0:
            max_even = temp
        temp += 1
    return max_even