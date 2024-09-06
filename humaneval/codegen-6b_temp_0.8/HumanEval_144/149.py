
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
    def is_whole_num(numerator, denominator):
        if numerator == "0" or denominator == "0":
            return True
        return int(numerator) / int(denominator) == int(numerator) / int(denominator)

    if (x == "0" or n == "0") or is_whole_num(x, n):
        return True

    x = x.split("/")
    n = n.split("/")
    if x[0] == "0" or n[0] == "0":
        return is_whole_num(x[1], n[1])
    return is_whole_num(x[0], n[1]) and is_whole_num(n[0], x[1])


