
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
    # You need to implement a function with two arguments: x and n
    # The function should check if both x and n are valid fractions
    # If both x and n are valid fractions, the function should check if the value of x/n is an integer
    # If the value of x/n is an integer, the function should return True
    # If the value of x/n is not an integer, the function should return False
    # You can use the modulus operator (%) to check if a number is an integer

    if not isinstance(x, Fraction) or not isinstance(n, Fraction):
        return False
    return x % n == 0