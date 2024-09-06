
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
    odd_digits = [n%10]
    while n > 9:
        n = n//10
        odd_digits.append(n%10)
    return 1 if odd_digits[0] % 2 == 1 else 0
