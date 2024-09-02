
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    count = 1
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
        count += 1
    product = 1
    for i in range(count):
        if digits[i] % 2!= 0:
            product *= digits[i]
    return product
