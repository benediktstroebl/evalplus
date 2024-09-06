```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    s1, s2 = min(s1), min(s2)
    e1, e2 = max(s1), max(s2)
    if e1 < s2 or e2 < s1:
        return "NO"
    else:
        intersect_length = e1 - s2 + 1
        if is_prime(intersect_length):
            return "YES"
        else:
            return "NO"
```

The function utilizes the `is_prime` helper function to determine if the intersection length is prime. It also handles cases where the intervals do not overlap by comparing the start and end points of each interval.