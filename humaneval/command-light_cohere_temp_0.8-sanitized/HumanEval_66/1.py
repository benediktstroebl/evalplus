def digitSum(s):
    return sum(chr(n) for n in range(64) if s[n] == chr(n))