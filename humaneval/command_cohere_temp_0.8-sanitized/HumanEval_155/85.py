def even_odd_count(num):
    count = 0
    # Iterate each digit in the input number
    for digit in str(num): 
        # Convert digit to int and check if it is even
        even = int(digit) % 2 == 0
        if even:
            count += 1
    return count, 2 - count