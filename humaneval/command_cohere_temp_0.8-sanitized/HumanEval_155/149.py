def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input should be an integer")
    
    digits = str(num)
    even_count = 0
    odd_count = 0
    
    for digit in digits:
        if digit == '0' or digit == '2' or digit == '4' or digit == '6' or digit == '8':
            even_count += 1
        elif digit == '1' or digit == '3' or digit == '5' or digit == '7' or digit == '9':
            odd_count += 1
        
    return (even_count, odd_count)