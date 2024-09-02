
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
    x = int(x)
    n = int(n)
    if x == 0 or n == 0:
        return False
    if x == 1 or n == 1:
        return True
    if x % n == 0:
        return False
    return True

test_cases = [
    ("1/5", "5/1"),
    ("1/6", "2/1"),
    ("7/10", "10/2"),
    ("3/4", "4/1"),
    ("22/29", "29/22")
]

for test_case in test_cases:
    x, n = test_case
    print(f"{test_case}: {simplify(x, n)}")