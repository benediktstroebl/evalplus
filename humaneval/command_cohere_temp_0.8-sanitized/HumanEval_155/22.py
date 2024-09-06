def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input should be an integer")
    
    counts = {True: 0, False: 0}
    
    for digit in str(num):
        if digit.isdigit():
            is_even = digit % 2 == 0
            counts[is_even] += 1
    
    return counts