def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    
    digits = str(num)
    even_count = 0
    odd_count = 0
    
    for digit in digits:
        if digit <= '9' and digit >= '0':
            if digit % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        else:
            raise ValueError("Input must be an integer")
    
    return (even_count, odd_count)