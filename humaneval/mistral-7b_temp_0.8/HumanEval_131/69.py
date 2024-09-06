
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Your code here
    return reduce(lambda x,y: x*y if not (x%2 or y%2) else x*y,[int(d) for d in str(n)]) or 0
