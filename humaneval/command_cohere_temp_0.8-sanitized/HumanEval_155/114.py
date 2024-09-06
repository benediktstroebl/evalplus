def even_odd_count(num):
    if isinstance(num, int): 
        count_even = 0
        count_odd = 0
        num_str = str(num)
        
        # Iterate through each digit in the number
        for digit in num_str:
            if digit == '0' or digit == '2' or digit == '4' or digit == '6' or digit == '8':
                count_even += 1
            elif digit == '1' or digit == '3' or digit == '5' or digit == '7' or digit == '9':
                count_odd += 1
        return (count_even, count_odd)
    else:
        raise ValueError("Input must be an integer")