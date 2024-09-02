
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
    # Example 1
    if n == x:
        return True
    # Example 2
    if n != x:
        if n % x == 0:
            return False
        if x % n == 0:
            return True
    # Example 3
    if n != x:
        if n % x == 0:
            return False
        if x % n == 0:
            return True
    # Example 4
    if n != x:
        if n % x == 0:
            return False
        if x % n == 0:
            return True