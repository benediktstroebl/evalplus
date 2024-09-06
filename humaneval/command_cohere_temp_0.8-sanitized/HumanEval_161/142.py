def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if not set(s) & set(letters):
        return s[::-1]
    return s.swapcase()