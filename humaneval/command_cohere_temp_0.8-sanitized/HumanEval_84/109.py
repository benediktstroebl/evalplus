def solve(n):
    s = str(n)
    return bin(int(''.join(s))).replace('0b', '')