def skjkasdkd(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))]
    return sum(map(int, str(max(primes, key = lambda x: x))))