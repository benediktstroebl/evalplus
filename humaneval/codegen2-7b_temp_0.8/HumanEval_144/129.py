
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
    if n[1] == 0:
        return False
    numerator = int(n[0])
    denominator = int(n[1])
    if numerator == 0:
        return False
    temp = int(x[0])
    if temp == 0:
        return False
    temp_den = int(x[1])
    temp_num = temp * temp_den
    if temp_den == denominator:
        return True
    if temp_num == numerator * denominator:
        return True
    
