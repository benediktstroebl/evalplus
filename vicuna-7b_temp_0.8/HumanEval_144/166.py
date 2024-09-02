
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
    # Create a list of all possible combinations of x and n
    x_numerators = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    n_denominators = ["1", "2", "3", "4", "5", "6", "10"]

    for i in range(len(x_numerators)):
        for j in range(len(n_denominators)):
            numerator = x_numerators[i]
            denominator = n_denominators[j]
            x_n = x*numerator/denominator
            if x_n.is_integer() and x_n.q == 1:
                return True
    return False