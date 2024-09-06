def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")

    count_even = 0
    count_odd = 0

    str_num = str(num)
    
    for char in str_num:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            count_even += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            count_odd += 1
    
    return (count_even, count_odd)