
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
    # Convert x and n to float to handle integer division
    x = float(x)
    n = float(n)

    # Check if x and n are integers
    if x % 1 == 0 and n % 1 == 0:
        return True

    # Check if x and n have a common denominator
    if not common_denominator(x, n):
        return False

    # Simplify the expression x \* n
    simplified = simplify_with_numerator_denominator(x, n)

    # Check if the simplified expression is a whole number
    if is_whole_number(simplified):
        return True

    return False
