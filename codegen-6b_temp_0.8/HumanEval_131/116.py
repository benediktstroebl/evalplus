
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    counter = {}
    n = str(n)
    if n[0] == '0':
        return 0
    for d in n:
        num = int(d)
        if num % 2 != 0:
            if d not in counter:
                counter[d] = 1
            else:
                counter[d] += 1
    return reduce(lambda x, y: x * y, counter.values())


add = 0
mult = 0
for x in range(1, 10**6):
    if digits(x) > 9:
        add += 1
    mult = max(mult, digits(x))
