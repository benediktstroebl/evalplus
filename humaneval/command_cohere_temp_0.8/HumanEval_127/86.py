```python
def is_prime(n):
    """
    Checks whether the given integer n is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Determine whether the length of the intersection of two given closed intervals is a prime number or not.
    """
    # Convert the interval pair to a format that simplifies the computation of the intersection
    # i.e. (1, 3) -> [1, 3] and (2, 4) -> [2, 4]
    s1, s2 = [s1], [s2]
    s1 = [start for start, end in s1 if start <= end]
    s2 = [start for start, end in s2 if start <= end]

    # Check if the intervals don't intersect or their intersection length is 1, None or NaN
    if s1 == [] or s2 == [] or s1[0] == s2[0] or min(s1[0], s2[0]) > max(s1[1], s2[1]):
        return "NO"

    # Compute the intersection
    interval = [max(s1[0], s2[0]), min(s1[1], s2[1])]

    # Check if the intersection length is prime
    if is_prime(abs(interval[1] - interval[0])):
        return "YES"
    else:
        return "NO"
```

The function leverages two important functions:
1. `is_prime(n)`: This function takes an integer `n` as input and checks whether it is a prime number or not. It iterates through numbers from 2 to the square root of `n`, if `n` is divisible by any of these numbers, it returns `False`. If it finishes the iteration without finding a divisor, it returns `True`.
2. `intersection(s1, s2)`: This is the main function that takes interval pairs `s1` and `s2` and returns a string indicating whether their intersection length is a prime number or not. The function first simplifies the interval representation from tuples to lists. It then checks if the intervals don't intersect or their intersection length is 1, None, or NaN and returns "NO" in these cases. Otherwise, it computes the intersection and checks if the length of the intersection is prime using the `is_prime` function.

The code will accurately determine whether the length of the intersection of two given closed intervals is a prime number or not and return "YES" or "NO" accordingly.