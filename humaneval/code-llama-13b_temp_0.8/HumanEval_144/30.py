
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
    def get_list(x):
        num_den = x.split("/")
        num_den = list(map(int, num_den))
        return num_den

    num_den1 = get_list(x)
    num_den2 = get_list(n)

    if num_den1[1] % num_den2[1] == 0:
        num_den1[0] *= num_den2[1]
        num_den1[1] *= num_den2[0]
        return num_den1[0] % num_den1[1] == 0
    else:
        return False

