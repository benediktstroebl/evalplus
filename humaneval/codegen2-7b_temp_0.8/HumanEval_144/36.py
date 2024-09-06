
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
    if not isinstance(x, str) or not isinstance(n, str):
        return
    if x == '0/0' or n == '0/0':
        return
    if '+' in x:
        x = x[x.index('+')+1:]
    if '+' in n:
        n = n[n.index('+')+1:]
    if x[0] == '0':
        x = x[1:]
    if n[0] == '0':
        n = n[1:]
    if int(x) * int(n) == 1:
        return True
    else:
        return False
    
