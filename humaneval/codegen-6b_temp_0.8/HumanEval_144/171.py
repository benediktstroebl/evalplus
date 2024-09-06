
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
    # convert to a list
    x_l = x.split('/')
    n_l = n.split('/')

    simplified_l = []
    for n_elem, x_elem in zip(n_l, x_l):
        n_int = int(n_elem)
        x_int = int(x_elem)
        simplified_l.append(str(n_int * x_int))

    d_l = []
    for n in simplified_l:
        if int(n) != 0:
            d_l.append(int(n))

    eval_str = '/'.join(d_l)

    try:
        return eval_str.split('/')[0] == eval_str.split('/')[1]
    except IndexError:
        return True

