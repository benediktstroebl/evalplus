
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Fast check for even digits
    if sum(map(lambda x: x % 2 == 0, str(n))) == 0:
        return 0
    
    # Get the string of the number
    digits = list(map(int, str(n)))
    # Get the odd digits
    odd_digits = digits[1:] if len(digits) > 1 else digits
    # Calculate the product
    return sum(x * y for x, y in zip(odd_digits, odd_digits[1:]))
