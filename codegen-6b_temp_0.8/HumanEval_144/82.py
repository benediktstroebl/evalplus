
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
    x_num, x_den = x.split('/')
    n_num, n_den = n.split('/')

    def simplify_helper(x, n):
        x_num, x_den = x.split('/')
        n_num, n_den = n.split('/')

        def check_num(num, n):
            num_num, num_den = num.split('/')
            if int(num_num) == 0:
                return True
            return simplify_helper(num, n)

        def check_den(den, n):
            den_num, den_den = den.split('/')
            if den_num == n_num and int(den_den) == 1:
                return True
            return simplify_helper(den, n)

        if x_den != n_den:
            return False

        if x_num == n_num:
            return True

        return check_den(n_den, x_num) or check_num(x_num, n_den)

    return simplify_helper(x, n)

