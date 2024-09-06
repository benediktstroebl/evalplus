
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
    def get_nums(str_repr):
        """Returns numerator and denominator
        of fraction given in string format"""
        numerator, denominator = str_repr.split('/')
        return int(numerator), int(denominator)

    def get_gcd(a, b):
        """Returns GCD of 2 integers"""
        return b if a == 0 else get_gcd(b % a, a)

    def get_lcm(a, b):
        """Returns LCM of 2 integers"""
        return a * b // get_gcd(a, b)

    x_numer, x_denom = get_nums(x)
    n_numer, n_denom = get_nums(n)

    x_new_denom = get_lcm(x_denom, n_denom)
    x_new_numer = x_numer * (x_new_denom // x_denom)

    n_new_denom = get_lcm(n_denom, x_denom)
    n_new_numer = n_numer * (n_new_denom // n_denom)

    x_new = x_new_numer // x_new_denom
    n_new = n_new_numer // n_new_denom

    return (x_new * n_new) % 1 == 0
