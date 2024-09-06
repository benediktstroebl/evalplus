
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
    x = x.split('/')
    n = n.split('/')

    def divide(x, n):
        if len(x) >= len(n):
            while len(x) > len(n):
                n.append(0)
            return [int(x[i]) / int(n[i]) for i in range(len(x))]
        return [int(n[i])/int(x[i]) for i in range(len(x))]

    def gcd(x):
        gcd = 1
        for i in x:
            if i == 0:
                gcd = 0
                break
            gcd = i
        return gcd

    def lcm(x, y):
        return x * y // gcd(x, y)

    def multiply(x, n):
        if n == 1:
            return x
        elif n % 2 == 1:
            return multiply(x, n - 1) * x
        else:
            return multiply(x, n / 2) ** 2

    if gcd(int(x[0]), int(n[0])) == 1:
        return True
    else:
        x = divide(x, n)
        if n[0] == 1:
            for i in range(1, len(x)):
                if x[i] != 1:
                    return False
        elif n[0] % 2 == 1:
            if (multiply(x, n[0]) - 1) % n[0] != 0:
                return False
        else:
            if multiply(x, n[0]) != 1:
                return False
        return True


assert simplify("1/5", "5/1") == True
assert simplify("1/6", "2/1") == False
assert simplify("7/10", "10/2") == False
assert simplify("1/7", "14/2") == True
assert simplify("5/7", "6/11") == True
assert simplify("1/11", "10/19") == True
