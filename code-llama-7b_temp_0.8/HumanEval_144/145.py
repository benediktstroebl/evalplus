
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

    # if x is "0/1", then n must be whole number
    if x == "0/1":
        return n.isdigit()

    # if n is "0/1", then x must be whole number
    if n == "0/1":
        return x.isdigit()

    # if x is whole number, then return if n is whole number
    if x.isdigit():
        return n.isdigit()

    # if n is whole number, then return if x is whole number
    if n.isdigit():
        return x.isdigit()

    # if x and n are fraction
    # if x / n is whole number, return True
    # else return False
    if is_whole_number(x, n):
        return True

    return False
