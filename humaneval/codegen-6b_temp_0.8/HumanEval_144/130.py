
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
    a, b = map(int, x.split('/')[0], x.split('/')[1])
    c, d = map(int, n.split('/')[0], n.split('/')[1])
    
    if b > d:
        a, b, c, d = b, a, d, c
    
    if a % d == 0:
        if int(a/d) == c:
            return True
        else:
            return False
    
    r = c * d
    divisors = [r, a, b]
    divisors.sort()
    
    remainders = [r, a % d, b % d]
    remainders.sort()
    
    if divisors[0] == remainders[0]:
        return True
    
    return False
