
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # base case: if all digits are even, return 0
    if sum(map(lambda x: x % 2 if x > 0, digits(n))) == 0:
        return 0
    
    # recursive case: if some digits are odd, return the product of the
    # odd digits and recur for the remaining digits
    return (sum(map(lambda x: x // 2 if x > 0, digits(n))) * digits(n // 2)) if n > 1 else n
