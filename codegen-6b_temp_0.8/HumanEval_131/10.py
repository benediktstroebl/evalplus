
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # BEGIN digits
    "*** YOUR CODE HERE ***"
    if n < 10:
        return n
    s = []
    while n:
        s.append(n % 10)
        n /= 10
    product = 1
    for i in range(len(s)):
        if s[i] % 2:
            product *= s[i]
    return product
    # END digits

