
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
    if n == "1" and x == "1":
        return True
    elif n == "1" and x == "0":
        return False
    elif x == "0":
        return False
    elif n == "1" and x == "2":
        return False
    else:
        if (x.split("/")[1] == n.split("/")[1]) and (int(x.split("/")[0]) * int(n.split("/")[0]) == int(x * n)):
            return True
        else:
            return False

test_case = [
    ("1/5", "5/1"),
    ("1/6", "2/1"),
    ("7/10", "10/2"),
    ("0", "1"),
    ("0", "2"),
    ("2", "1")
]
for i in test_case:
    t = i[0]
    n = i[1]
    result = simplify(t, n)
    print(result)