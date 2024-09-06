def solve(n):
    s = str(n)
    return bin(sum(int(d) for d in s))[2:][:len(s)]