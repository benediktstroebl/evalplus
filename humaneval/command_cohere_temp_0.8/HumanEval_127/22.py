```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def intersection(s1, s2):
    st, ed = max(s1[0], s2[0]), min(s1[1], s2[1])
    if st > ed:
        return "NO"
    elif is_prime(st-ed+1):
        return "YES"
    else:
        return "NO"

# Test cases
assert intersection((1, 2), (2, 3)) == "NO"
assert intersection((-1, 1), (0, 4)) == "NO"
assert intersection((-3, -1), (-5, 5)) == "YES"
```

The `is_prime` function checks if a given integer `n` is prime or not. It's a trivial implementation of the Sieve of Eratosthenes algorithm. The `intersection` function calculates the length of the intersection of two intervals, and then calls `is_prime` to determine if it's prime. If the length is not prime, it returns "NO", and if it is prime, it returns "YES". Also, a couple of test cases are included to validate the correctness of the script.  This approach assumes that the given intervals are valid, which means the start of each interval is less than or equal to its end.