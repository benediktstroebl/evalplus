def solve(n):
    s = str(n)
    return ''.join([str(int(s[i: i+3]) ^ int(s[i+2: i+5])) for i in range(0, len(s), 3)])