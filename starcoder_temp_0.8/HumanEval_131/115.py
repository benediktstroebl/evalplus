
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    assert n >= 0
    nums = [int(d) for d in str(n)]
    product = 1
    for n in nums:
        if n % 2 == 1:
            product *= n
    return product
