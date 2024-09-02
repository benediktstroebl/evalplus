
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
    def get_num_den(x):
        return [int(i) for i in x.split('/')]
    
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def is_simplify(x, n):
        num1, den1 = get_num_den(x)
        num2, den2 = get_num_den(n)
        
        lcm = (den1 * den2) // gcd(den1, den2)
        
        return (lcm % (num1 * num2)) == 0
    
    return is_simplify(x, n)
