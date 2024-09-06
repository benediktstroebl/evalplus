
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
    def list_to_str(lst):
        return "/".join([str(item) for item in lst])

    def str_to_list(strng):
        return [int(item) for item in strng.split("/")]

    x_list = str_to_list(x)
    n_list = str_to_list(n)
    return x_list[0] * n_list[1] % x_list[1] == 0 and n_list[0] * x_list[1] % n_list[1] == 0

