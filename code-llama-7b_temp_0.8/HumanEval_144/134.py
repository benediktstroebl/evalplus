
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

    # FIXME: The time complexity is N^2, where N is the length of the longer string.
    # Implement a linear time algorithm.
    x_numerator, x_denominator = map(int, x.split('/'))
    n_numerator, n_denominator = map(int, n.split('/'))

    if x_denominator % n_denominator == 0:
        # Simplify by dividing by the denominator of n
        x_numerator = x_numerator * (x_denominator // n_denominator)
        x_denominator = n_denominator

    if n_numerator % x_denominator == 0:
        # Simplify by dividing by the denominator of x
        n_numerator = n_numerator * (n_denominator // x_denominator)
        n_denominator = x_denominator

    x = f"{x_numerator}/{x_denominator}"
    n = f"{n_numerator}/{n_denominator}"

    x_numerator, x_denominator = map(int, x.split('/'))
    n_numerator, n_denominator = map(int, n.split('/'))

    if (x_numerator % n_denominator == 0 and x_denominator % n_numerator == 0 and
        x_numerator // n_denominator == n_numerator // n_denominator):
        return True

    return False

