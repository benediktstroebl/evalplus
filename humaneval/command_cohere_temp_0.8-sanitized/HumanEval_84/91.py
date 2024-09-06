def solve(n):
    s = str(n)
    return '{0:b}'.format(sum(int(d) for d in s))