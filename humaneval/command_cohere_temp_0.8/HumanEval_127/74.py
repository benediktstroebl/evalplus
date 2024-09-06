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
```

The approach uses a simple algorithm to check if the intersection interval is prime. Additionally, a check is implemented for edge cases where intervals don't intersect or have start and end values identical, and returns "NO" in such cases. To implement this, the `is_prime` helper function is used, which utilizes a well-known algorithm to check for prime numbers. This method is used to ascertain whether the length of the intersection of two intervals is a prime number, and then returns "YES" or "NO" based on this evaluation.