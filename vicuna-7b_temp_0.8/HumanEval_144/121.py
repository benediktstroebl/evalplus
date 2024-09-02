
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
    # Create a variable to store the simplified value
    simplified_value = None

    # Compare the numerators of the two fractions
    if x[0] == n[0]:
        # If they have the same numerator, compare the denominators
        if x[1] == n[1]:
            # If they have the same denominator, return True
            simplified_value = True
        else:
            # If they don't have the same denominator, return False
            simplified_value = False
    else:
        # If they don't have the same numerator, return False
        simplified_value = False

    return simplified_value
