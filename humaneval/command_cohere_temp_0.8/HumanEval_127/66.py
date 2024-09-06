```python
def is_prime(n):
    """
    Checks if a number is prime

    Args:
        n (int): Number to check if it's prime

    Returns:
        bool: True if n is prime, otherwise False
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Check if the intersection of two intervals is a prime number

    Args:
        s1 (tuple): First interval (start, end)
        s2 (tuple): Second interval (start, end)

    Returns:
        str: "YES" if the intersection is prime, otherwise "NO"
    """
    if max(s1[0], s1[1]) > min(s2[0], s2[1]) or min(s1[0], s1[1]) < max(s2[0], s2[1]):
        return "NO"
    else:
        x = max(s1[1], s2[1]) - min(s1[0], s2[0])
        if is_prime(x):
            return "YES"
        else:
            return "NO"
```

The `is_prime` function checks if a number is prime using the 'for' loop to iterate through the numbers from 2 to the square root of the number and checking for divisibility. 

The `intersection` function calculates the length of the intersection of two intervals and then calls `is_prime` to check if this length is prime. If it is prime, it returns "YES"; otherwise, it returns "NO". Also, the function returns "NO" if the intervals do not intersect.

You can use it by calling `intersection((1, 2), (2, 3))`, which should return "NO" as an example use.