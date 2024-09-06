
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = []
    for num in str(n):
        if int(num) % 2 == 0:
            digits.append(0)
        else:
            digits.append(int(num))
    if digits == [0,0,0]:
        return 0
    else:
        return (reduce(lambda x, y: x*y, digits))
