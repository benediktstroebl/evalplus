def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(s) == 0 or set(s) & set(letters) == set() else ''.join(c.swapcase() if c in letters else c for c in s)