def even_odd_count(num):
    """Return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    temp_num = abs(num)

    while temp_num != 0:
        digit = temp_num % 10
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        temp_num = temp_num // 10
    
    return (count_even, count_odd)