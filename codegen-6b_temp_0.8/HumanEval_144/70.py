
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
    s1, s2 = x.split('/')
    b, a = n.split('/')
    if not s1.isdigit():
        return False
    if not s2.isdigit():
        return False
    if not b.isdigit():
        return False
    if not a.isdigit():
        return False

    s1, s2 = int(s1), int(s2)
    b, a = int(b), int(a)
    return s1 * b * a / (b * a - s2 * b) == s1 * a * b / (a * b - s2 * a)
    # return a.isdigit() and b.isdigit() and s1.isdigit() and s2.isdigit() and not (s2 == 0 and a/b == 0) and a/b > 0 and float(a/b) == float(a/b)


assert simplify("1/5", "5/1") is True
assert simplify("1/6", "2/1") is False
assert simplify("7/10", "10/2") is False
assert simplify("1/6", "3/5") is True

assert simplify("1/5", "5/11") is True
assert simplify("1/6", "2/4") is False
assert simplify("7/10", "2/5") is True
assert simplify("1/6", "1/3") is True
assert simplify("1/6", "4/5") is False
