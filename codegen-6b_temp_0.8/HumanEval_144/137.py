
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
    x = x.split('/', 1)[0]
    n = n.split('/', 1)[0]
    if n == '1':
        return x == '1'
    if x == '0':
        return n == '1'
    numerator, denominator = x, n
    numerator, denominator = min(x, n), max(x, n)
    first_digit, second_digit = numerator[0], denominator[0]
    if first_digit == second_digit:
        return (numerator[1:] == denominator[1:])
    elif first_digit < second_digit and numerator[1:] == denominator[1:]:
        return True
    else:
        return False
