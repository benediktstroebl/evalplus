
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
    # Try both x and n as string and convert to float
    try:
        x = float(x)
    except ValueError:
        return False
    try:
        n = float(n)
    except ValueError:
        return False

    # Convert both x and n to int
    x = int(x)
    n = int(n)

    # Check if the product is an integer
    if x * n == int(x * n):
        return True

    # Check if the difference is less than 1
    diff = abs(int(x * n) - x * n)
    if diff <= 1:
        return False

    return True