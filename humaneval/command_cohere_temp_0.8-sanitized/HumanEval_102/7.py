def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    
    if min_even == max_even or max_even % 2 == 0:
        return max_even
    
    return -1