
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
    # Check if x is integer
    try:
        int(x)
        return True
    except ValueError:
        pass

    try:
        int(n)
        return True
    except ValueError:
        pass

    x_split = x.split('/')
    n_split = n.split('/')
    x_numerator = int(x_split[0])
    x_denominator = int(x_split[1])
    n_numerator = int(n_split[0])
    n_denominator = int(n_split[1])

    if x_numerator * n_denominator == x_denominator * n_numerator:
        return True
    else:
        return False
