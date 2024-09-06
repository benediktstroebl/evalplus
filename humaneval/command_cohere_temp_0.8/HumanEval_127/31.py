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
        return "YES" if is_prime(ed - st + 1) else "NO"

# Unit tests:
assert intersection((1, 2), (2, 3)) == "NO"
assert intersection((-1, 1), (0, 4)) == "NO"
assert intersection((-3, -1), (-5, 5)) == "YES"
```

The `is_prime` function is a helper used to determine if a given integer `n` is prime. This function uses a combination of small prime numbers (`2`, `3`, and `5`) to check for divisibility, moving forward by 6 each time (`i += 6`) to cover a wide range of potential divisors. This approach is more efficient than checking all potential divisors up to `n`. 

The `intersection` function calculates the intersection of two intervals, determining the start and end points of the intersection based on the supplied closed intervals, then deferrs to `is_prime` to determine if the length of the intersection is prime. 

The test suite provides examples from the problem statement to ensure the function behaves as expected.