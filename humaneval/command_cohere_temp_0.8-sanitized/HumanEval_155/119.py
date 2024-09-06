def even_odd_count(num):
    count = 0
    # Convert integer to string
    num_str = str(num)
    # Initialize the count of even and odd digits to 0
    even_count = 0
    odd_count = 0
    # Iterate through each digit in the number
    for digit in num_str:
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)