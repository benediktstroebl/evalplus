
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
    numerator, denominator = [int(x) for x in x.split('/')]
    d = gcd(numerator, denominator)
    if d != 1:
        numerator /= d
        denominator /= d
    
    numerator = str(numerator)
    denominator = str(denominator)
    a = numerator.split('.')[1]
    b = denominator.split('.')[1]
    
    a = a.ljust(n, '0')
    b = b.ljust(n, '0')
    
    n = numerator.ljust(n, '0')
    d = denominator.ljust(n, '0')        
    
    if a == b:
        return True
    return False

