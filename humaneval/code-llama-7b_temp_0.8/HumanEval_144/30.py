
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
    import re

    # for simplicity, we assume x is always <numerator>/<denominator>
    x_numerator, x_denominator = map(int, re.findall(r"\d+", x))
    n_numerator, n_denominator = map(int, re.findall(r"\d+", n))

    # check if x * n is a whole number
    whole_number_flag = (x_numerator * n_denominator) % n_numerator == 0

    return whole_number_flag

