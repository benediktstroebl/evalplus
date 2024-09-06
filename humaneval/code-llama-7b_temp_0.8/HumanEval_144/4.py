
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

    # Convert x, n to numerator and denominator
    x_num, x_den = x.split("/")
    n_num, n_den = n.split("/")

    # Make x and n the fraction with the greatest denominator
    if int(x_den) < int(n_den):
        x_num, x_den = n_num, n_den
        n_num, n_den = x.split("/")
    elif int(x_den) > int(n_den):
        n_num, n_den = x_num, x_den
        x_num, x_den = n.split("/")

    # Calculate GCD
    gcd = 0
    for i in range(1, int(x_den) + 1):
        if int(x_den) % i == 0 and int(n_den) % i == 0:
            gcd = i

    # Return if x * n is a whole number
    return (int(x_num) * int(n_num)) % gcd == 0
