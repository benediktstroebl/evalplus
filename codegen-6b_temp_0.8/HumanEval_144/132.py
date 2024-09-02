
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
    import fractions

    def is_simplified(x, n):
        try:
            return int(x) == int(fractions.Fraction(x, n))
        except:
            return False

    def get_num(n):
        return n.split('/')[0] or 1

    def get_den(n):
        return n.split('/')[1] or 1

    num_n = get_num(n)
    num_x = get_num(x)
    den_n = get_den(n)
    den_x = get_den(x)

    if x == '0' or n == '0':
        return False

    if is_simplified(num_n / den_n, num_x / den_x):
        return True

    if is_simplified(num_x / den_x, num_n / den_n):
        return True

    return False
