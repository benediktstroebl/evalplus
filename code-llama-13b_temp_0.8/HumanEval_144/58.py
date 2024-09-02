
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
    def make_fraction(frac_str):
        return [int(i) for i in frac_str.split('/')]

    def is_whole(frac_str):
        return not make_fraction(frac_str)[1] % make_fraction(frac_str)[0]
    
    def lcm(frac_1, frac_2):
        a, b = make_fraction(frac_1)
        c, d = make_fraction(frac_2)
        return (a * d, b * c)

    return is_whole(x) and is_whole(n) and is_whole(str(lcm(x, n)))
