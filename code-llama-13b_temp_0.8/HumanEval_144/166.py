
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
    def get_num(s):
        if not s:
            return 0
        return int(s[0])

    def get_den(s):
        if not s:
            return 1
        return int(s[1])

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    a, b = x.split("/")
    c, d = n.split("/")
    num_x = get_num(a) * get_den(c)
    den_x = get_num(b) * get_den(d)
    num_n = get_num(c) * get_den(a)
    den_n = get_num(d) * get_den(b)
    if gcd(den_x, den_n) == den_x:
        return num_x / num_n * den_x == int(num_x / num_n * den_x)
    return False

