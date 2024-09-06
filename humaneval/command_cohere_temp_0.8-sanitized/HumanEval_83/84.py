def starts_one_ends(n):
    s = str(n)
    return sum(int(s[i] == '1' for i in range(n)) for m in (s, s[::-1]))