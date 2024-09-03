def digitSum(s):
    return sum(chr(n) == ord(c) for n, c in enumerate(reversed(s)))