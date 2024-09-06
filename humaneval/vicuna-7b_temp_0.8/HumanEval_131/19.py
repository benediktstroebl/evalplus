
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # check for even numbers
    if sum(map(int, str(n))) % 2 == 0:
        return 0
    
    # handle the base case
    if n < 10:
        return n
    
    # handle the recursive case
    d = n // 10
    n = n % 10
    # use the above function to compute the product of the odd digits
    return digits(d) * 10 + digits(n)
