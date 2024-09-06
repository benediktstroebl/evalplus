def solve(N):
    s = str(N)
    return '{0:b}'.format(sum(int(d) for d in s))