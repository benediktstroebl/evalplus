
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
    numerator = int(n.lstrip("0"))
    denominator = int(n.rstrip("0"))
    if numerator > 0 and denominator > 0:
        return True
    return x == str(numerator / denominator)


assert simplify("1/5", "5/1") is True
assert simplify("1/6", "2/1") is False
assert simplify("7/10", "10/2") is False
assert simplify("2/6", "1/3") is True
assert simplify("2/6", "5/4") is True
assert simplify("2/6", "6/5") is True
assert simplify("2/6", "8/5") is False
assert simplify("2/6", "3/4") is False
assert simplify("8/5", "3/4") is True
assert simplify("8/5", "5/4") is True
assert simplify("8/5", "2/4") is False
assert simplify("2/4", "8/5") is False
assert simplify("7/3", "2/3") is True
assert simplify("1/3", "2/3") is False
assert simplify("1/3", "3/2") is True
