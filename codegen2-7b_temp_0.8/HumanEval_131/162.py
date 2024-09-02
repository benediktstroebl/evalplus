
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    odd = sum(int(i) for i in str(n))
    if odd % 2!= 0:
        return odd
    return digits(odd//2)
