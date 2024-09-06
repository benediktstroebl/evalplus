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
    smin = max(s1[0], s2[0])
    smax = min(s1[1], s2[1])
    if smin > smax:
        return "NO"
    if is_prime(smax - smin + 1):
        return "YES"
    else:
        return "NO"
```

The function `intersection()` takes two interval arguments, `s1` and `s2`, and returns "YES" if the length of their intersection is a prime number, "NO" otherwise. The prime checking function `is_prime()` is used for verification.