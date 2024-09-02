
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
    # Check if both x and n have a common denominator
    if abs(x.denominator * n.denominator) > 1:
        return False
    
    # Check if n is a multiple of x
    if n.numerator % x.numerator == 0:
        return True
    
    # Otherwise, check if x and n have a common factor other than 1
    for i in range(max(len(x.numerator), len(n.numerator))):
        if x.numerator[i] == n.denominator[i] and x.denominator[i] != 0:
            return True
    
    # If none of the above conditions are met, the result is not a whole number
    return False
