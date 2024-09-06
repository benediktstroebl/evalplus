
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    s = str(n)
    for i in range(len(s)):
        if s[i] % 2 == 1:
            return int(s[i:]) * (i + 1)
    
