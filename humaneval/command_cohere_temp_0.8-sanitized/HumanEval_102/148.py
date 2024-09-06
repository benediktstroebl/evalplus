def choose_num(x, y):
    max_even = -1
    temp_num = x
    check_even = 2

    while temp_num <= y:
        if temp_num % 2 == 0:
            if max_even < temp_num:
                max_even = temp_num
        temp_num += 1

    if max_even == -1:
        return -1
    else:
        return max_even