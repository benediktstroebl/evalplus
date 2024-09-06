```python
def is_prime(n):
    """
    Checks whether a number is prime
    Args:
        n (int): Number to check
    Returns:
        bool: Whether n is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Checks whether the intersection of two intervals is prime
    Args:
        s1 (tuple): First interval (start, end)
        s2 (tuple): Second interval (start, end)
    Returns:
        str: "YES" if prime, "NO" if not
    """
    if not (s1[0] <= s2[1] and s2[0] <= s1[1]):
        return "NO"
    else:
        intersect_start = max(s1[0], s2[0])
        intersect_end = min(s1[1], s2[1])
        intersect_len = intersect_end - intersect_start
        if is_prime(intersect_len):
            return "YES"
        else:
            return "NO"
```

The function uses a separate function, `is_prime`, to optimize the primality test. It also checks for invalid inputs and avoids repetition. The `is_prime` function uses a optimized approach of checking divisors up to the square root. Would you like to know more about these algorithms?