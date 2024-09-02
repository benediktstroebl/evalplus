
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
    def is_whole(x):
        return x.count('/') == 1

    def is_whole_neg(x):
        return x.count('/') == 0

    def split_fr(x):
        l = x.split('/')
        return l[0], l[1]

    numerator, denominator = split_fr(x)
    num = int(numerator)
    den = int(denominator)
    if is_whole(x):
        return True
    if is_whole_neg(x):
        return False
    if num > den:
        return True
    g = gcd(num, den)
    return (num // g, den // g)
