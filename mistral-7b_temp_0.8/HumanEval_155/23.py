
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Initialize counters
    even_count = 0
    odd_count = 0
    # Loop through the number
    for digit in str(num):
        # Check if digit is even
        if int(digit) % 2 == 0:
            even_count += 1
        # Check if digit is odd
        elif int(digit) % 2 == 1:
            odd_count += 1
    # Return a tuple with the number of even and odd digits
    return (even_count, odd_count)
