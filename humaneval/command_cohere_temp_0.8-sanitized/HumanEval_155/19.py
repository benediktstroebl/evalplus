def even_odd_count(num):
    count = 0
    # Iterate each digit in the input number
    for digit in str(num): 
        # increment count if digit is odd
        if digit % 2 != 0: 
            count += 1 
    return count, 10 - count