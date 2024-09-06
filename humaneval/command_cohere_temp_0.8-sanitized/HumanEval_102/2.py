def choose_num(x, y):
    max_even = -1
    max_even_found = False
    
    for num in range(x, y + 1):
        if num % 2 == 0 and (max_even < num or max_even_found == False):
            max_even = num
            max_even_found = True
    
    return max_even if max_even_found else -1