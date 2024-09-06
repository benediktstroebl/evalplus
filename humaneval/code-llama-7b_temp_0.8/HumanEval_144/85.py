
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
    num_x, den_x = x.split('/')
    num_n, den_n = n.split('/')

    # Multiply numerator and denominator by the common denominator
    new_num_x = int(num_x) * int(den_n)
    new_num_n = int(num_n) * int(den_x)

    # Get the GCD of the numerator
    gcd = get_gcd(new_num_x, new_num_n)

    # Check if it is a whole number
    return (new_num_x / gcd) == (new_num_n / gcd)

