def even_odd_count(num):
    count_even = 0
    count_odd = 0
    num_str = str(num)
    
    # Iterate through each digit in the integer representation
    for digit in num_str:
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    
    return (count_even, count_odd)