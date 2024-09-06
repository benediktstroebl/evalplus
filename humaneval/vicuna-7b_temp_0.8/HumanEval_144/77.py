
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
    # Add x and n
    x_numerator = int(x)
    x_denominator = int(x[1])
    n_numerator = int(n)
    n_denominator = int(n[1])

    # Check if x and n are equal
    if x_numerator == n_numerator and x_denominator == n_denominator:
        return True

    # Check if x is a factor of n
    if x_numerator != 0 and n_numerator % x_numerator == 0:
        return True

    # If x and n are not equal and x is not a factor of n, then x * n is not a whole number
    return False
