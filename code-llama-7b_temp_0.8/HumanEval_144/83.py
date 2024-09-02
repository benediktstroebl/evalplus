
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
    # Get numerator and denominator from x and n
    x_numerator, x_denominator = x.split("/")
    n_numerator, n_denominator = n.split("/")
    x_numerator, x_denominator, n_numerator, n_denominator = int(x_numerator), int(x_denominator), int(n_numerator), int(n_denominator)

    # Multiply x and n
    x_mult_n = x_numerator * n_denominator
    n_mult_x = n_numerator * x_denominator

    # Check if multiplication result is a whole number
    if x_mult_n == n_mult_x:
        return True
    return False
