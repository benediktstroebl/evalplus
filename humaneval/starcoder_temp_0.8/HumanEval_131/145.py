
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
    else:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n = int(n / 10)
        odds = 1
        for digit in digits:
            if digit % 2 == 1:
                odds *= digit
        return odds

