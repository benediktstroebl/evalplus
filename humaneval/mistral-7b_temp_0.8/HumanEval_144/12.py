
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

    # Split the strings by '/' and convert each of the two elements to float
    numerator1, denominator1 = map(float, x.split('/'))
    numerator2, denominator2 = map(float, n.split('/'))

    # Calculate the product of the numerators and the product of the denominators
    numerator = numerator1 * numerator2
    denominator = denominator1 * denominator2

    # Return True if the product of the numerators is a whole number and the product of the denominators is also a whole number
    return (numerator == int(numerator)) and (denominator == int(denominator))

