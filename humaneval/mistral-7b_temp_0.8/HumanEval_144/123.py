
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

    # Convert both fractions to integers
    x_int = int(x)
    n_int = int(n)

    # Find the least common multiple (LCM) of the denominator and the divisor
    lcm = x_int * n_int

    # Simplify the fraction by dividing the numerator by the LCM
    simplified_fraction = x_int // lcm

    # Return True if the simplified fraction is an integer and False otherwise
    return simplified_fraction.is_integer()

