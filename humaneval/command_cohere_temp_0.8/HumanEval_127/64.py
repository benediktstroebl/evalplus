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
    st, en = max(s1[0], s2[0]), min(s1[1], s2[1])
    if st > en:
        return "NO"
    elif is_prime(st - s1[0] + s2[0]) and is_prime(en - st + 1):
        return "YES"
    else:
        return "NO"
```

The approach uses a simple algorithm to determine if the intersection's length is prime. The function `is_prime` determines whether a given integer is prime. It returns 'YES' if the length of the intersection is prime and 'NO' if it is not. It returns 'NO' if the intervals do not overlap. To determine if the result is prime, the algorithm uses a mixture of checks to rule out divisibility by small numbers and a '6k +/- 1' divisibility rule.