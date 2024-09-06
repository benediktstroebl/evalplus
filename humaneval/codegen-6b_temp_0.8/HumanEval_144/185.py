
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
    numerator = int(x[:x.index('/')])
    denominator = int(x[x.index('/') + 1:])
    quotient = int(numerator / denominator)
    return (numerator % denominator == 0)


assert simplify('1/5', '5/1') is True
assert simplify('1/6', '2/1') is False
assert simplify('7/10', '10/2') is False
assert simplify('35/18', '12/5') is True

assert simplify('1/5', '5/1') is True
assert simplify('1/6', '2/1') is False
assert simplify('7/10', '10/2') is False
assert simplify('35/18', '12/5') is True

assert simplify('10/3', '3/2') is True
assert simplify('8/3', '2/1') is False
assert simplify('32/5', '5/2') is False
