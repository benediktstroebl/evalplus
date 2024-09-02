
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

    if not x or not n: return False
    if x == '0': return '0'
    if x == '1': return '1'
    x = str(x)
    n = str(n)
    
    numerator = int(x.split("/")[0])
    denominator = int(x.split("/")[1])
    numerator_n = int(n.split("/")[0])
    denominator_n = int(n.split("/")[1])

    if (denominator % denominator_n == 0) and (numerator % numerator_n == 0):
        return True
    else:
        return False

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
