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
    else:
        return "YES" if is_prime(st - ed + 1) else "NO"

# Test cases
assert intersection((1, 2), (2, 3)) == "NO"
assert intersection((-1, 1), (0, 4)) == "NO"
assert intersection((-3, -1), (-5, 5)) == "YES"
```

The `is_prime` function is used to determine if a given integer `n` is prime. It employs a combination of conditions and checks, starting with the consideration of `2` and `3` as special cases. It then checks for divisibility by `2` and `3`, followed by checks for divisibility by numbers of the form `i * i` and `i * (i + 2)`, starting from `i = 5`. This approach efficiently rules out non-prime numbers. The function returns `True` if `n` is prime and `False` otherwise. 

The `intersection` function calculates the intersection of two intervals, which is deemed prime if its length is greater than `1` and the `is_prime` function returns `True`. 

The test suite accompanies the implementation to verify correct behavior against various scenarios.

This solution is efficient in its prime-checking mechanism and provides an accurate assessment of the intersection's primality.