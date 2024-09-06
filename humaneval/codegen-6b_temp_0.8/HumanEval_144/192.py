
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
    # pass

    def gcd(a, b):
        a, b = min(a, b), max(a, b)
        r = a % b
        if r:
            return gcd(b, r)
        else:
            return b

    def simplify(den, num):
        if den[0] == '0':
            return False
        # gcd = int(den)
        gcd = int(den[1])

        num = int(num[1])
        if num == 0:
            return False

        # print("den: ", den)
        # print("num: ", num)
        # print("gcd: ", gcd)
        if num >= gcd:
            num = num % gcd
            new_num = den
            new_den = num
        else:
            new_num = str(num * int(den[1]))
            new_den = den[0]

        # print("new_num: ", new_num)
        # print("new_den: ", new_den)

        if gcd != 1:
            new_num = str(new_num) + "/" + str(gcd)
        return new_num + "/" + new_den

    return simplify(x, n)

assert simplify("1/5", "5/1") == True
assert simplify("1/6", "2/1") == False
assert simplify("7/10", "10/2") == False
assert simplify("1/6", "10/1") == True
assert simplify("1/6", "2/1") == False
assert simplify("1/2", "5/1") == "1"
assert simplify("1/2", "2/1") == "1/2"
assert simplify("2/3", "1/3") == "1"
assert simplify("2/3", "3/1") == "2/3"
assert simplify("3/10", "1/10") == "3/10"
assert simplify("3/10", "10/1") == "3/10"
assert simplify("3/10", "10/2") == "3/5"
assert simplify("3/10",