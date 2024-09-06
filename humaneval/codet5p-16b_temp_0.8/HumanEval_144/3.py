
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

    if x.find('/') < 0 or n.find('/') < 0:
        return None

    numerator = int(x[:x.find('/')])
    denominator = int(n[:n.find('/')])
    simplified_num = numerator * denominator // math.gcd(numerator, denominator)
    simplified_den = denominator // math.gcd(numerator, denominator)
    return x.find('/') == n.find('/') and int(x[x.find('/')+1:]) == 0 and int(n[n.find('/')+1:]) == 0
