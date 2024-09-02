
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
    # Create a map to store the fractions
    fractions = {}

    # Iterate over the string representations of x and n
    for i in range(len(x)):
        # Split the string at each position to get the numerator and denominator
        numerator, denominator = map(int, x[i].split("/"))
        # Try to find a fraction in the map that matches the numerator and denominator
        fraction = fractions[numerator/denominator]
        if fraction is None:
            return False
        # If the fraction is found, return True
        return True