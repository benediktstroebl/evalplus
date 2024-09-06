
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
    def fraction(s):
        # if n = '7/10' and x = '1/2'
        # remove the leading and trailing characters from the string
        # using split() and the first element
        # and then remove leading and trailing spaces
        # then remove the decimal point
        num, den = s.split('/')[0], s.split('/')[1]
        num = num.strip()
        den = den.strip()
        den = den.rstrip('0')
        num = num.rstrip('0')

        f = Fraction(num, den)
        return f

    def gcd_frac(a, b):
        return a if not b else gcd_frac(b, a % b)

    def simplify_frac(a, b):
        if a == b:
            return True
        if a.numerator == 0 or b.numerator == 0:
            return False
        if a.denominator == 0 or b.denominator == 0:
            return False
        if a.denominator == 1:
            return True
        if b.denominator == 1:
            return True
        return a.numerator / b.numerator == a.denominator / b.denominator

    def lcm_frac(a, b):
        return a * b // gcd_frac(a, b)

    def get_common_denominator(a, b):
        return a * b // gcd_frac(a, b)

    def get_reduced_fraction(a, b):
        return a * int(b.denominator / a.denominator)

    def reduce_frac(a, b):
        common = get_common_denominator(a, b)
        numerator = get_reduced_fraction(a, common)
        denominator = get_reduced_fraction(b, common)
        return numerator, denominator

    def calc_num(a, b):
        num, den = reduce_frac(a, b)
        c = simplify_frac(num, den)
        return c

    def get_numerator(s