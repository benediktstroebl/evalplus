
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

    assert isinstance(x, str) and isinstance(n, str), "Both x and n must be strings"

    # Part 1: Convert to rational numbers
    x_rat = int(x.split("/")[0]) / int(x.split("/")[1])
    n_rat = int(n.split("/")[0]) / int(n.split("/")[1])

    # Part 2: Simplify rational numbers
    x_rat_simplified = math.gcd(x_rat, n_rat)
    n_rat_simplified = x_rat / x_rat_simplified

    # Part 3: Convert to fraction
    x_simplified = str(int(x_rat_simplified)) + "/" + str(int(x_rat_simplified))
    n_simplified = str(int(n_rat_simplified)) + "/" + str(int(n_rat_simplified))

    return x_simplified == n_simplified

