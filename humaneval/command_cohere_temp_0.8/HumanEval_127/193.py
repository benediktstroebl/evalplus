```python
def is_prime(n):
    """
    Checks if a number is prime
    """
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
    """
    Determine if the length of the intersection of two closed intervals is prime
    """
    if not (s1[0] <= s2[1] and s1[1] >= s2[0]):
        return "NO"
    interval_length = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if is_prime(interval_length):
        return "YES"
    else:
        return "NO"
```

The function utilizes the `is_prime` function to determine if the length of the intersection of two closed intervals is a prime number or not. To do so, it checks if the intervals overlap, calculating the length of the intersection, and passes it to is_prime for prime checking. The function returns "YES" if the length is prime and "NO" otherwise.