def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input should be an integer")
    
    count = 0
    num_str = str(num)
    
    for char in num_str:
        if char != ' ':
            if char <= '9' and char >= '0':
                if char % 2 == 0:
                    count += 1
                else:
                    count += 0
            else:
                count += 0
    
    return count, num_str