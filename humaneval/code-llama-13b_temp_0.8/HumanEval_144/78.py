
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

    # I simply split the two numbers by the / symbol and then multiply and compare the result to the original fraction.
    def _convert_to_number(fraction):
        return int(fraction.split("/")[0]) / int(fraction.split("/")[1])

    result = _convert_to_number(x) * _convert_to_number(n)
    return result == int(result)
