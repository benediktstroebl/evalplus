def digits(n):
    """Return the product of the odd digits in the integer n."""
    result = 0
    for digit in str(n):
        if int(digit) % 2 == 1: 
            result *= int(digit)
    return result if result else 0