def even_odd_count(num):
    count_even = 0
    count_odd = 0
    num_str = str(num)
    
    # Iterate through each digit in the number and categorize them as odd or even
    for digit in num_str:
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
            
    return (count_even, count_odd)