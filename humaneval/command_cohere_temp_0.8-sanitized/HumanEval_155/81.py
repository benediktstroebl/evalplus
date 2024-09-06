def even_odd_count(num):
    digit_dict = {}
    count_even = 0
    count_odd = 0

    for digit in str(num):
        if digit in digit_dict:
            digit_dict[digit] += 1
        else:
            digit_dict[digit] = 1
        
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
            
    return (count_even, count_odd)