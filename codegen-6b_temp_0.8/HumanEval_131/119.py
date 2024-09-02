
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Initialize product to 1
    result = 1
    # Stuff the digits into a list
    digits = [int(i) for i in str(n)]
    # Loop through the list
    for i in digits:
        # Check for even number
        if i % 2 != 0:
            # Multiply by the current element
            result *= i
    # Return result
    return result

