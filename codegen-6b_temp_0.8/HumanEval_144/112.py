
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
    def factornum(x):
        factors = []
        for m in range(2, int(x ** 0.5) + 1):
            if x % m == 0:
                factors.append(m)
                factors.append(int(x / m))
        return factors

    def gcd(num1, num2):
        if num2 == 0:
            return num1
        else:
            return gcd(num2, num1 % num2)

    def lcm(num1, num2):
        return num1 * num2 / gcd(num1, num2)

    def simplify(fract, nstring):
        num = int(nstring[0] + '1')
        if simplify(fract, str(num)) == False:
            return False
        return True

    def checknum(num, nnum):
        if num == 1 or nnum == 1:
            return True
        if num == 0 or nnum == 0:
            return False
        if num == 1 and nnum == 1:
            return gcd(num, nnum) == 1
        if num == nnum:
            return True
        if num > nnum:
            for m in range(2, nnum + 1):
                if num % m == nnum % m:
                    return False
            if lcm(num, nnum) == num:
                return True
            else:
                return False
        else:
            for m in range(2, num + 1):
                if nnum % m == num % m:
                    return False
            if lcm(num, nnum) == nnum:
                return True
            else:
                return False

    x, n = str(x), str(n)
    if x == n:
        return True
    if n == '1':
        return True
    if '/' not in x and '/' not in n:
        return False
    fract, nstring = x.split('/')[0], x.split('/')[1]
    if '/' not in n:
        n = n + '/' + '1'
    else:
        fract, nstring = n