
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
    # Convert x and n to integers
    x_int = int(x)
    n_int = int(n)

    # Check if both x and n are integers
    if x_int == n_int:
        # If both are integers, return True
        return True

    # Check if either x or n is not an integer
    if x_int != n_int:
        # If not, return False
        return False

    # Check if x is less than n
    if x_int < n_int:
        # If x is less than n, return False
        return False

    # Check if n is divisible by x
    if n_int % x_int == 0:
        # If n is divisible by x, return True
        return True

    # If none of the above conditions are met, return False
    return False