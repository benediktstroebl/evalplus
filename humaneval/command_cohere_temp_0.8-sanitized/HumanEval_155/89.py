def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input should be an integer")
    
    digits = str(num)
    count_even = sum(1 for digit in digits if digit in '02468')
    count_odd = sum(1 for digit in digits if digit in '13579')
    
    return (count_even, count_odd)