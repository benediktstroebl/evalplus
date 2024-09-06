def even_odd_count(num):
    """Return the number of even and odd digits in the integer num."""
    # Convert num to a string
    num_str = str(num)
    # Initialize the count of even and odd digits to 0
    even_count = 0
    odd_count = 0
    # Iterate over each digit in the num_str
    for digit in num_str:
        # If the digit is even, increment the even_count
        if digit % 2 == 0:
            even_count += 1
        # If the digit is odd, increment the odd_count
        else:
            odd_count += 1
    # Return a tuple of even and odd counts
    return (even_count, odd_count)