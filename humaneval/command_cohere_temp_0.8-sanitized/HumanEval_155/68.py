def even_odd_count(num):
    count = 0
    # Convert integer to string
    num_str = str(num)
    # Initialize the count of even and odd digits to 0
    even_count = 0
    odd_count = 0

    for char in num_str:
        if char > '9':
            # Character is larger than 9, it's an exponent or a character from NaN
            # Assuming these cases to be odd, as they are uncommon
            odd_count += 1
        elif char % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)