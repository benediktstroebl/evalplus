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
    Determine if the intersection of two intervals is prime
    """
    if not isinstance(s1, tuple) or not isinstance(s2, tuple):
        raise TypeError("Both arguments should be tuples")
    if min(s1[0], s1[1]) > max(s2[0], s2[1]):
        return "NO"
    intersection_start = max(s1[0], s2[0])
    intersection_end = min(s1[1], s2[1])
    intersection_length = intersection_end - intersection_start
    if intersection_length < 2:
        return "NO"
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
```

The function `intersection()` takes in two tuple inputs, `s1` and `s2`, which represent two closed intervals. It first performs some input validation to check if the tuples actually represent valid intervals. Then, it calculates the length of the intersection of these intervals and checks if this length is greater than 1. Finally, it determines if the length of the intersection is prime, returning "YES" if so, and "NO" otherwise. 

The `is_prime()` function is meant to check if a given number is prime. It's used in the `intersection()` function to check if the length of the intersection is prime. This is a standard prime-checking function that works by checking if the number is divisible by small primes (2, 3, 5, 7, 11, 13, ...) up to its square root.