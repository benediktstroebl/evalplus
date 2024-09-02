
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = []
    total = 0
    while n > 0:
        digits.append(n % 10)
        n //= 10
    for i in range(len(digits)):
        if digits[i] % 2 != 0:
            total = total * digits[i]
    return total


