
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

    # Check if x and n are valid fractions
    if not x.isdigit() or not n.isdigit():
        return False

    # Split x and n into numerator and denominator
    numerator = int(x.split("/")[0])
    denominator = int(x.split("/")[1])
    other_numerator = int(n.split("/")[0])
    other_denominator = int(n.split("/")[1])

    # Calculate the product of the numerators and the product of the denominators
    product_numerator = numerator * other_numerator
    product_denominator = denominator * other_denominator

    # Check if the product of the numerators is divisible by the product of the denominators
    if product_numerator % product_denominator == 0:
        return True
    else:
        return False
