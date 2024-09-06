
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
    def find_pair(s):
        """Given an expression, it returns the position of the first pair of '/'.
        Note: The expression can be of any length.
        """
        for i, c in enumerate(s):
            if c == '/':
                return i
        return -1

    if x[0] == '/':
        return False
    if n[0] == '/':
        return False

    x = x.replace('/', '')
    n = n.replace('/', '')

    pos_pair = find_pair(x)
    if pos_pair == -1:
        return True
    if pos_pair + 1!= len(x):
        return
