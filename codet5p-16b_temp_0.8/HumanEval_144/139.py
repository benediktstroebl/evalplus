
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

    import re
    
    n_regex = re.compile('^([0-9]+)/([0-9]+)$')
    x_regex = re.compile('^([0-9]+)')
    
    if not n_regex.match(n):
        raise ValueError
    
    if not x_regex.match(x):
        raise ValueError
    
    n_num = int(n.split('/')[0])
    n_den = int(n.split('/')[1])
    x_num = int(x.split('/')[0])
    x_den = int(x.split('/')[1])
    
    result = x_num * n_num / x_den * n_den
    
    return result == int(result)

