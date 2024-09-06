def solve(n):
    s = str(n)
    return ''.join([str(int(s[i:i+1])).count('1') for i in range(0, len(s), 1)])