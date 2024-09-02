
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

    def eval(a,b,n,x):
        """Your task is to implement a function that will check if x * n evaluates to a whole number.
        Return True if x * n evaluates to a whole number and False otherwise. Both x and n, are string
        representation of a fraction, and have the following format, <numerator>/<denominator> where both numerator
        and denominator are positive whole numbers.

        You can assume that x, and n are valid fractions, and do not have zero as denominator.

        eval("1/5", "5/1") = True
        eval("1/6", "2/1") = False
        eval("7/10", "10/2") = False
        """
        if a == "0" or b == "0":
            return False
        else:
            a = int(a)
            b = int(b)
            n = int(n)
            x = int(x)
            if (a * n) / b == x:
                return True
            else:
                return False
    return eval(x, n
