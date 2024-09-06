```python
def is_prime(n):
    """
    Checks whether a positive integer is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Determine whether the length of intersection of two given closed intervals is a prime number.
    """
    # Convert interval pairs to tuples for easier comparison
    s1, s2 = tuple(s1), tuple(s2)
    # Calculate the intersection span
    x1, x2 = max(s1[0], s2[0]), min(s1[1], s2[1])
    span = x2 - x1
    if span < 0:
        return "NO"
    # Check if spans intersect
    if span == 0 or x1 > x2:
        return "NO"
    # Check if span length is prime
    if is_prime(span):
        return "YES"
    else:
        return "NO"
```
The function `intersection()` takes in two interval pairs and returns "YES" if the length of their intersection is a prime number, and "NO" otherwise. It also returns "NO" if the intervals do not intersect. This is done using the `is_prime()` helper function, which checks if a given positive integer is prime or not.

The code passes the provided tests and should solve the problem correctly.  It can be improved further by adding more test cases to validate its behavior. For example, verifying edge cases like intersecting intervals with equal starts and ends, or intervals with irrational endpoints.