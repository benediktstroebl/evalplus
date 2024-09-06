
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Hint: use % operator to check the last digit
    # Hint: also check your loop condition

    result = 1
    for x in range(len(str(n))):
        if int(str(n)[x]) % 2 != 0:
            result *= int(str(n)[x])

    return result

