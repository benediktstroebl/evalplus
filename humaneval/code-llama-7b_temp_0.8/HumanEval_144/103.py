
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
    # Numerator and denominator of x
    num_x, denom_x = x.split("/")

    # Numerator and denominator of n
    num_n, denom_n = n.split("/")

    # GCD of numerator and denominator of x
    gcd_x = gcd(int(num_x), int(denom_x))

    # GCD of numerator and denominator of n
    gcd_n = gcd(int(num_n), int(denom_n))

    # Simplifying
    num_x = int(num_x) // gcd_x
    num_n = int(num_n) // gcd_n
    denom_x = int(denom_x) // gcd_x
    denom_n = int(denom_n) // gcd_n

    # Return true if x * n evaluates to a whole number, and false otherwise
    return denom_x == denom_n and (num_x * num_n) % denom_n == 0

