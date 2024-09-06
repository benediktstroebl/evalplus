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
    elif is_prime(st - s1[0] + s2[0]) and is_prime(en - st):
        return "YES"
    else:
        return "NO"
```

The approach uses the `is_prime` helper function to check whether the length of the intersection of two intervals is a prime number or not. If the start and end of the intersection are the same, meaning that the two intervals overlap completely, it returns "YES" if the size of the overlap is prime, and "NO" otherwise. Otherwise, it returns "NO" instantly.