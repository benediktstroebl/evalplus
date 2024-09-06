
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
    # Here we convert the input x and n to float using the built-in function float()
    # This allows us to perform arithmetic operations with them.
    x = float(x)
    n = float(n)

    # We check if the result of the multiplication is a whole number
    # If it is, we return True
    if (x * n).is_integer() and (x * n) == int(x * n):
        return True

    return False