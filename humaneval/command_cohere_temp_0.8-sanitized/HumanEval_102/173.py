def choose_num(x, y):
    max_even = -1
    limit = y - x + 1
    
    for num in range(x, y + 1):
        if num % 2 == 0 and num > max_even:
            max_even = num
    
    return max_even if max_even <= limit else -1