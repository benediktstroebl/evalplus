def even_odd_count(num):
    if not isinstance(num, int):
        return "Input should be an integer"
    
    count_even = 0
    count_odd = 0
    
    str_num = str(num)
    
    for char in str_num:
        if char == '0' or char == '1' or char == '2' or char == '3':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        else:
            return "Invalid input. Input should be an integer."
    
    return (count_even, count_odd)