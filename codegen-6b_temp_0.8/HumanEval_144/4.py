
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
    def proc_frac(x, y):
        """
        Helper function that processes the fraction by removing the common
        factor of the denominator which is a whole number.
        """
        if y == "1":
            return int(x)
        i = int(x)
        j = int(y)
        return i * j / gcd(i, j)

    x = proc_frac(x, n)
    n = proc_frac(n, n)
    return x == n or x == int(x)

