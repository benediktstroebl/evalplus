import math
def skjkasdkd(lst):
    primes = [x for x in lst if math.prime(x)]
    return sum(map(int, str(max(primes))))