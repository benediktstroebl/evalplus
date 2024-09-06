def fizz_buzz(n):
    return sum(int(d) == 7 for d in str(i) if i % 11 == 0 or i % 13 == 0 and i < n)