
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
    # ##### BEGIN SOLUTION ########################################################
    # def return_whole_number(a, b):
    #     return int(a * b) == int(a) * int(b)
    
    # x, n = x.replace('/', ' ').split(), n.replace('/', ' ').split()
    # eg = x + n if int(n[0]) > 0 else x
    # return True if return_whole_number(x[0], n[0]) else False
    return str(int(x) * int(n) / gcd(x, n)).lower() == x
    # return str(int(x) * int(n) / gcd(x, n)).lower() == x
    # return str(int(x) * int(n) / gcd(x, n)).lower() == x
    # ##### END SOLUTION #########################################################
