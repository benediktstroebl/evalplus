
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
    
    # ----- First Solution -----
    if '/' not in x:
        return int(x) == int(n)
    
    x_numerator, x_denominator = x.split('/')
    n_numerator, n_denominator = n.split('/')
    
    x_numerator = int(x_numerator)
    x_denominator = int(x_denominator)
    n_numerator = int(n_numerator)
    n_denominator = int(n_denominator)
    
    gcd_val = gcd(x_numerator, x_denominator, n_numerator, n_denominator)
    
    x_numerator = x_numerator / gcd_val
    x_denominator = x_denominator / gcd_val
    n_numerator = n_numerator / gcd_val
    n_denominator = n_denominator / gcd_val
    
    gcd_val = gcd(x_numerator, x_denominator, n_numerator, n_denominator)
    
    x_numerator = int(x_numerator / gcd_val)
    x_denominator = int(x_denominator / gcd_val)
    n_numerator = int(n_numerator / gcd_val)
    n_denominator = int(n_denominator / gcd_val)
    
    if x_numerator * n_numerator >= 0:
        return True
    else:
        return False
    
    
    # ----- Second Solution -----
    """After you have simplified x and n, simplify the resulting fraction again. There are several ways to simplify the resulting fraction, and all of them are equally valid. You can choose a suitable one and return True or return False as the result.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") =