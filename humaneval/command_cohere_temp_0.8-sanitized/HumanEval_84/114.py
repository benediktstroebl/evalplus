def solve(n):
    s = str(n)
    return ''.join([str(int(s[i:i+1]) + int(s[i:i+1])%2) for i in range(len(s))])