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
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Check if the intersection of two intervals is prime

    Args:
        s1 (tuple): First interval (start, end)
        s2 (tuple): Second interval (start, end)

    Returns:
        str: "YES" if the intersection is prime, otherwise "NO"
    """
    if max(s1[0], s1[1]) > min(s2[0], s2[1]) or max(s2[0], s2[1]) > min(s1[0], s1[1]):
        return "NO"
    else:
        interval_length = max(s1[1], s2[1]) - min(s1[0], s2[0])
        if is_prime(interval_length):
            return "YES"
        else:
            return "NO"
```

The function uses a separate function, `is_prime`, to check if the parameter is prime. The `is_prime` function loops from 2 to the square root of the number and checks if the number is divisible by any integer in that range. If the number is not divisible by any number, then it is prime.  The `intersection` function checks if the intervals overlap and if so, it calculates the length of the intersection and passes this length to the `is_prime` function. If the length of the intersection is prime, the function returns "YES"; otherwise, it returns "NO".  This approach helps to avoid duplicate code and makes the code more reusable and maintainable.