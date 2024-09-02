
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    
    if n < 10:
        return n
    
    last_digit = n % 10
    
    if last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8:
        return 0
    
    return 10 * digits(n // 10) + last_digit

