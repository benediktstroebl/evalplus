
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
    x_num, x_den = x.split('/')
    n_num, n_den = n.split('/')

    # We want to make sure that we only have positive whole numbers here
    x_num, x_den, n_num, n_den = map(abs, [x_num, x_den, n_num, n_den])

    # This is a good case to use the gcd function
    common = gcd(int(x_num), int(n_den))

    # We can now simplify our fractions
    new_x = int(x_num) // common * int(n_den)
    new_n = int(n_num) // common * int(x_den)

    # We need to check if the new fractions can be simplified
    common = gcd(new_x, new_n)

    # If they can be simplified, then it is a whole number
    if common != 1:
        new_x //= common
        new_n //= common

    return str(new_x) + '/' + str(new_n)
