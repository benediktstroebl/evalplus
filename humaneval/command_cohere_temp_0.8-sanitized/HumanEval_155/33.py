def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input num is not an integer")
    
    count_even = 0
    count_odd = 0
    
    str_num = str(num)
    
    for char in str_num:
        if char == '0' or char == '1' or char == '2' or char == '3':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        elif char == '-' or char == '+' or char == 'e' or char == 'E':
            continue
        else:
            raise ValueError(f"Unexpected character encountered in num: {char}")
    
    return (count_even, count_odd)