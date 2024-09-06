
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
    a = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0,}
    b = {'1/': 1, '2/': 2, '3/': 3, '4/': 4, '5/': 5, '6/': 6, '7/': 7, '8/': 8, '9/': 9, '0/': 0,}
    a1 = x[1]
    b1 = n[1]
    a1 = int(a1)
    b1 = int(b1)
    a1 = a1 * b1
    a2 = x[0]
    b2 = n[0]
    a2 = int(a2)
    b2 = int(b2)
    a2 = a2 * b2
    if a1 == a2:
        return True
    return False

"""
    if x[1] == n[1]:
        return True
    else:
        return False
"""
