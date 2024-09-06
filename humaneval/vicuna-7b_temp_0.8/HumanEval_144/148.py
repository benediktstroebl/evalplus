
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
    # Function to check if the fraction is equal to 1
    def check_if_fraction_is_one(x):
        return x.numerator == 1 and x.denominator == 1

    # Function to check if the fraction is simplified
    def check_if_fraction_is_simplified(x):
        return x.numerator == x.denominator

    # Function to perform the actual simplification
    def perform_simplification(x, n):
        if check_if_fraction_is_one(x):
            return True
        if check_if_fraction_is_simplified(n):
            return True
        if check_if_fraction_is_simplified(x):
            return True
        if (n.numerator * x.denominator).is_integer() and (x.numerator * n.denominator).is_integer():
            return True
        return False

    return perform_simplification(x, n)