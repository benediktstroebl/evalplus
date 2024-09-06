
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    numx, denx = x.split('/')
    numy, deny = n.split('/')

    # simplify fraction x
    if int(denx) == 0:
        return False
    while int(numx) != 0:
        numx, denx = (int(numx) + int(denx)) / 2, int((int(denx) + int(numx)) / 2)
    numx, denx = str(numx), str(denx)

    # simplify fraction y
    if int(deny) == 0:
        return False
    while int(numy) != 0:
        numy, deny = (int(numy) + int(deny)) / 2, int((int(deny) + int(numy)) / 2)
    numy, deny = str(numy), str(deny)

    # return True if simplified x * y is whole number
    if int(numx) * int(numy) % int(deny) == 0:
        return True
    return False

