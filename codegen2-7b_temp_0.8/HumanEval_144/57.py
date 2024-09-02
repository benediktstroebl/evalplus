
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
    num = x.split('/')
    if num[0].isdigit() and num[1].isdigit():
        if (int(num[0]) == 0 and int(num[1]) == 0):
            return False
        return (int(num[0]) * int(num[1])) == int(num[0]) / int(num[1])
    else:
        
