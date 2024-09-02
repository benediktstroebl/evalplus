
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
    n_str = n.split("/")
    x_str = x.split("/")

    # print(f"x_str: {x_str}")
    # print(f"n_str: {n_str}")
    x_numer = int(x_str[0])
    x_denom = int(x_str[1])
    n_numer = int(n_str[0])
    n_denom = int(n_str[1])
    # print(f"x_numer: {x_numer}")
    # print(f"x_denom: {x_denom}")
    # print(f"n_numer: {n_numer}")
    # print(f"n_denom: {n_denom}")

    # print(f"x_numer * n_denom == x_denom * n_numer: {x_numer * n_denom == x_denom * n_numer}")

    if x_numer * n_denom == x_denom * n_numer:
        return True
    else:
        return False

