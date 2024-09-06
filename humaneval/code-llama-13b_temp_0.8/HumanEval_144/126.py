
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
    def extract(x):
        x = x.split("/")
        return [int(i) for i in x]
    
    def lcm(x, y):
        return x * y / gcd(x, y)

    def gcd(x, y):
        return x if y == 0 else gcd(y, x % y)
    
    x = extract(x)
    n = extract(n)
    
    l = lcm(x[1], n[1])
    c = l / x[1] * x[0]
    d = l / n[1] * n[0]
    return c * d % l == 0
