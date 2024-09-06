
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

    
    def gcd(a,b):
        while b:
            a, b = b, a%b
        return a
    if x == "0" or n == "0":
        return False
    if x == n:
        return True
    num = int(x.split("/")[0])
    den = int(x.split("/")[1])
    num1 = int(n.split("/")[0])
    den1 = int(n.split("/")[1])
    g = gcd(num, den)
    g1 = gcd(num1, den1)
    if g == g1 and den % g == 0 and den1 % g1 == 0:
        return True
    else:
        return False
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
