
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # your code here
    count = 0
    sum = 0
    while n > 0:
        digit = n%10
        if digit % 2 != 0:
            sum += digit
            count += 1
        n = n // 10
    if count > 0:
        return sum
    else:
        return 0
