
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
    fraction = x.split("/")
    numerator = fraction[0]
    denominator = fraction[1]
    numerator, denominator = int(numerator), int(denominator)

    if n == '1':
        return True
    elif n == '0':
        return False

    if n.isdigit():
        n = int(n)
        if numerator % n == 0:
            return True
        else:
            return False

    numerator, denominator = map(int, [numerator, denominator])
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd

    # check if gcd divides the numerators, otherwise set the numerators to 1
    if numerator % gcd != 0 or denominator % gcd != 0:
        numerator, denominator = 1, 1

    numerator, denominator = furx(numerator, denominator, n)

    if numerator == denominator == 1:
        return True
    else:
        return False

