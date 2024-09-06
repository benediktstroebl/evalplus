def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 and x != 1]
    return sum(map(int, str(max(primes))))