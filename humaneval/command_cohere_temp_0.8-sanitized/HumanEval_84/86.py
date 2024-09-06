def solve(n):
    s = str(n)
    return ''.join([str(int(bit)) for bit in s if bit != '0'])