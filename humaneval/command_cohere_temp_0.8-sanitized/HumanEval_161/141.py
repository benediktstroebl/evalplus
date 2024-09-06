def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(s) != len(set(s)) or not s.isalpha() else ''.join(c.swapcase() if c in letters else c for c in s)