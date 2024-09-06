
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
    # print(x, type(x))
    # print(n, type(n))
    # print(x.split("/")[0], type(x.split("/")[0]))
    # print(n.split("/")[0], type(n.split("/")[0]))

    first_num, first_denom = x.split("/")
    second_num, second_denom = n.split("/")

    if int(first_num) * int(second_denom) == int(first_denom) * int(second_num):
        return True
    return False
