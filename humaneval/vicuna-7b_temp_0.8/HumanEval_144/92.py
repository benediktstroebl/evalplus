
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
    if n == "1" or n == "0":
        return False
    if x == "1" or x == "0":
        return False
    if x == n:
        return True
    if n % 1 != 0:
        return True
    if n / 1 in {3, 4, 5, 6}:
        return True
    if x / 1 in {3, 4, 5, 6}:
        return True
    if x % 1 == 0 and x != n:
        return True
    if n % 10 in {3, 4, 5, 6, 7, 8, 9}:
        return True
    return False
