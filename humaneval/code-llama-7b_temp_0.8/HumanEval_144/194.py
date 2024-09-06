
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
    x_num = int(x.split("/")[0])
    x_den = int(x.split("/")[1])

    n_num = int(n.split("/")[0])
    n_den = int(n.split("/")[1])

    # Simplify fractions
    gcd = max(x_num, x_den, n_num, n_den)

    while True:
        if x_num % gcd == 0 and x_den % gcd == 0:
            x_num /= gcd
            x_den /= gcd
        else:
            break

        if n_num % gcd == 0 and n_den % gcd == 0:
            n_num /= gcd
            n_den /= gcd
        else:
            break

    x_simplified = str(x_num) + "/" + str(x_den)
    n_simplified = str(n_num) + "/" + str(n_den)

    if x_simplified == n_simplified:
        return True
    else:
        return False
