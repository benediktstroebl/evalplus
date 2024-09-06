def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")

    count_even = 0
    count_odd = 0

    str_num = str(num)
    
    for char in str_num:
        if char <= '9' and char >= '0':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        else:
            # Ignore non-digit characters
            continue
    
    return (count_even, count_odd)