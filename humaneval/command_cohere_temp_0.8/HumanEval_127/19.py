```python
def is_prime(n):
    """
    Checks whether a number is prime

    Args:
        n (int): Number to check
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Checks whether the intersection of two intervals is a prime number

    Args:
        s1 (tuple): First interval (start, end)
        s2 (tuple): Second interval (start, end)

    Returns:
        str: "YES" if the intersection is prime, "NO" otherwise
    """
    x = max(max(s1), max(s2)) - min(min(s1), min(s2))
    if x <= 0:
        return "NO"
    if is_prime(x):
        return "YES"
    else:
        return "NO"
```

The logic behind the code is quite straightforward. 
1. The `is_prime` function checks whether a given number is prime or not using a basic primality check algorithm.
2. The `intersection` function calculates the length of the intersection of the two given intervals.
3. If the length of the intersection is not positive (i.e., no intersection or overlapping), it returns "NO".
4. If the length of the intersection is prime, it returns "YES".
5. If the length of the intersection is not prime, it returns "NO".

This way, the code solves the problem by checking whether the intersection of two intervals is prime based on the provided specifications.