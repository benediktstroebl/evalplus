
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    odd = [1, 3, 5, 7, 9]
    for i in str(n):
        if int(i) in odd:
            product *= int(i)
        elif int(i) % 2 == 0:
            continue
        else:
            return 0
    return product

