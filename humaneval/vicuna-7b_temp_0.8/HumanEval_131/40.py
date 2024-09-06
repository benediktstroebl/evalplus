
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = max(n, 1)
    digits = [0] * n
    for i in range(n-1, -1, -1):
        if (n % i) % 2 == 0:
            digits[i] = 0
        else:
            digits[i] = i * (i-1) // 2
    return sum(digits)
