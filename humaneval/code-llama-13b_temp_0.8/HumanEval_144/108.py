
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
    # Split fractions into numerator and denominator
    x_split = x.split("/")
    n_split = n.split("/")

    # Calculate multiplied fraction
    numerator = int(x_split[0]) * int(n_split[0])
    denominator = int(x_split[1]) * int(n_split[1])

    # Return true if multiplied fraction equals integer
    if numerator / denominator == int(numerator / denominator):
        return True

    # Else return false
    return False
