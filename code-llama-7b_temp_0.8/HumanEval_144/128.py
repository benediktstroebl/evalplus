
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
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    def simplify_fraction(x, n):
        # Your code here
        x_numerator, x_denominator = x.split("/")
        n_numerator, n_denominator = n.split("/")
        x_numerator = int(x_numerator)
        x_denominator = int(x_denominator)
        n_numerator = int(n_numerator)
        n_denominator = int(n_denominator)

        x_denominator = int(x_denominator)
        n_denominator = int(n_denominator)

        multiplier = gcd(x_denominator, n_denominator)

        x_numerator = x_numerator * int(n_denominator / multiplier)
        n_numerator = n_numerator * int(x_denominator / multiplier)

        x = x_numerator
        n = n_numerator

        print(x)
        print(n)

        return (x % n) == 0

    return simplify_fraction(x, n)

