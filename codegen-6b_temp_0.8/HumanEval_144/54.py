
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
    (numerator, denominator) = fraction_to_number(x)
    (numerator_int, denominator_int) = fraction_to_integer(x)
    if numerator_int == 0:
        return True
    if n == "":
        return False
    (numerator_int2, denominator_int2) = fraction_to_integer(n)
    if numerator_int2 == 0:
        return True
    if denominator_int2 == 0:
        return False
    return int(numerator_int) * int(denominator_int) == int(numerator_int2) * int(denominator_int2)

