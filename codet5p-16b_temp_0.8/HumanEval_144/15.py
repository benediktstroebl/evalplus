
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

    if not n:
        return False
    if not x:
        return False

    if len(n) > len(x):
        x, n = n, x

    x = list(map(int, x.split('/')))
    n = list(map(int, n.split('/')))

    while n:
        divider = n.pop()
        if divider == 0:
            return False

        while x and divider < x[-1]:
            x.pop()
        if x and divider % x[-1] == 0:
            x[-1] = divider // x[-1]
        else:
            x.append(divider)

    return all(not x[i] % x[i-1] for i in range(1, len(x)))

