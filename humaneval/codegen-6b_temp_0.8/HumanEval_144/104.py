
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
    def recurse(x, n):
        if (x, n) not in memo:
            if (x == "0" or n == "0"):
                memo[(x, n)] = True
            else:
                # x is a whole number
                if int(x) == 0: return True
                # n is a whole number
                if int(n) == 0: return False
                # x, n are divisible, we want to simplify n
                div = int(x) / int(n)
                if div == 0 or div == 1:
                    memo[(x, n)] = True
                elif div != 0:
                    memo[(x, n)] = recurse(int(x) / int(n), int(n))
        return memo[(x, n)]

    memo = {}
    return recurse(x, n)
