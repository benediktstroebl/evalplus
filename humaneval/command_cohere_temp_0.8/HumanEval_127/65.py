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
    s1_end = s1[1]
    s2_start = s2[0]
    if s1_end < s2_start:
        return "NO"
    if s2_start > s1_end:
        return "NO"
    intersection_length = abs(s1_end - s2_start)
    if not is_prime(intersection_length):
        return "NO"
    return "YES"
```

The function `is_prime` is used to determine if a number is prime. This is a standard primality test. The function `intersection` calculates the length of the intersection of two intervals and then calls `is_prime` to determine if this length is prime. If it is prime, it returns "YES"; otherwise, it returns "NO". Also, note that this assumes that the intervals are sorted.