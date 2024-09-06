def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(s) == 0 or all(c not in letters for c in s) else ''.join(c.swapcase() if c in letters else c for c in s)