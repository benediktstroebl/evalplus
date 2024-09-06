```python
def is_prime(n):
    """
    Checks whether a positive integer 'n' is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Checks whether the length of the intersection of two closed intervals is a prime number or not.
    """
    interval1, interval2 = sorted([s1, s2]), [s1[0], s2[0]]
    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return "NO"
    interval_length = max(0, min(interval1[1], interval2[1]) - max(interval1[0], interval2[0]))
    if not is_prime(interval_length):
        return "NO"
    else:
        return "YES"
```

The function uses a separate `is_prime` function to check if the only values that are prime are solely the inputs that are intersected. It also handles cases where the intervals do not intersect or handle cases where the intersected interval is not a prime number.

Make sure to have a math library installed to avoid runtime errors when using the `is_prime` function. The `is_prime` function is a re-implementation of the `is_prime` function from the `math` library.