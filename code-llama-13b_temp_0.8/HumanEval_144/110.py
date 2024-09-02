
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

    # def is_valid(s):
    #     """
    #     :param s: String
    #     :return: Bool
    #     """
    #     num, den = s.split('/')
    #     num = int(num)
    #     den = int(den)
    #     return num / den > 0

    # return is_valid(x) and is_valid(n) and int(eval(x) * eval(n)) == eval(x) * eval(n)

    num_x, den_x = x.split('/')
    num_n, den_n = n.split('/')

    num_x = int(num_x)
    den_x = int(den_x)
    num_n = int(num_n)
    den_n = int(den_n)

    if num_x / den_x > 0 and num_n / den_n > 0 and int(num_x * num_n / den_x / den_n) == (num_x * num_n / den_x / den_n):
        return True
    else:
        return False

