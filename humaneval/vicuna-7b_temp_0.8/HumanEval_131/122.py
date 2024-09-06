
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # handle the special case of all digits being even
    if all(c in "04689" for c in str(n)):
        return 0
    # handle the special case of only the last digit being odd
    if str(n)[-1] in "9":
        return n * digits(n // 10)
    # handle the rest of the cases
    else:
        product = 1
        for i in range(1, len(str(n))):
            if str(n)[i] in "04689":
                product *= 10
            else:
                product *= str(n)[i]
        return product

n = int(input().strip())
result = digits(n)
