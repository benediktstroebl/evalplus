def choose_num(x, y):
    max_even = -1
    max_odd = -1
    
    for num in range(x, y + 1):
        if num % 2 == 0:
            if num > max_even:
                max_even = num
        else:
            if num > max_odd:
                max_odd = num
    
    if max_even == -1 and max_odd == -1:
        return -1
    elif max_even != -1:
        return max_even
    else:
        return max_odd