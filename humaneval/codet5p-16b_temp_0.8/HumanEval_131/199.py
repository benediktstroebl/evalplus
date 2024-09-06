
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    listOfDigits = list(str(n))
    result = 1
    for num in listOfDigits:
        if int(num) % 2 == 1:
            result *= int(num)
    return result
