
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
    if x == "0" or n == "0":
        return False
    numerator, denominator = str(x).split("/")
    numerator, denominator = int(numerator), int(denominator)
    simplified_numerator = numerator
    simplified_denominator = denominator
    for i in range(2, numerator):
        if numerator % i == 0 and denominator % i == 0:
            simplified_numerator = numerator // i
            simplified_denominator = denominator // i
    if simplified_numerator * simplified_denominator == numerator * denominator:
        return True
    
