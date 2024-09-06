
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

    # Split the numerator and denominator from x and n
    x_numerator, x_denominator = x.split('/')
    n_numerator, n_denominator = n.split('/')

    # Multiply them together, then simplify the result
    x_multiplied = int(x_numerator) * int(n_numerator)
    x_divided = x_multiplied / int(x_denominator)

    # Turn the result into a string
    x_simplified = str(x_divided)

    # Split the numerator and denominator of the simplified result
    x_simplified_numerator, x_simplified_denominator = x_simplified.split('/')

    # Compare the simplified result to the input
    if int(x_simplified_denominator) == int(n_denominator):
        return True
    return False
