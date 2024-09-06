def fizz_buzz(n):
    return sum(int(d) == 7 for d in str(n) if n % 11 == 0 or n % 13 == 0)