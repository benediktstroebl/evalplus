```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def intersection(s1, s2):
    st, ed = max(s1[0], s2[0]), min(s1[1], s2[1])
    if st > ed:
        return "NO"
    elif is_prime(st - ed + 1):
        return "YES"
    else:
        return "NO"

# Example usage
print(intersection((1, 2), (2, 3))) == "NO"
print(intersection((-1, 1), (0, 4))) == "NO"
print(intersection((-3, -1), (-5, 5)) == "YES")
```

The approach uses a simple algorithm for primality testing of a given number n. The algorithm is called the `6k ± 1` algorithm because it tests all numbers that are 6k ± 1 for prime candidacy. The algorithm removes candidates that have divisors in the range [2, 6k + 2] because they can be at most partially multiplied to give n, leaving the remaining candidates to be prime. A detailed explanation and proof of the algorithm can be found [here](https://cp-algorithms.com/primefactors/prime_factors.html). 

The rest of the code follows the problem statement and returns the appropriate response. Feel free to ask any questions or clarifications.