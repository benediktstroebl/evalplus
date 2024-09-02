
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Convert the number to digits
    digits = str(n)
    # Find the first digit that is odd
    odd_pos = digits.find(str(int(digits[:1] + digits[1:]) % 2)) + 1
    # If all digits are even, return 0
    if all(c in '0' for c in digits[odd_pos:]) == True:
        return 0
    # Otherwise, return the product of the odd digits
    return int(digits[:odd_pos]) * int(digits[odd_pos+1:])
