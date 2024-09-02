
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
    #your code here

    x_numerator = int(x[0:x.find('/')])
    x_denominator = int(x[x.find('/')+1:])
    n_numerator = int(n[0:n.find('/')])
    n_denominator = int(n[n.find('/')+1:])
    x_numerator *= n_denominator
    n_numerator *= x_denominator
    print(x_numerator)
    print(n_numerator)
    if x_numerator%n_numerator == 0:
        print(True)
    else:
        print(False)
