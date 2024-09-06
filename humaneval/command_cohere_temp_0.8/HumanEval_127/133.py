```python
def is_prime(n):
    """
    Checks if a number is prime
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
    # Convert the interval pair to a tuple of (start, end)
    interval = (max(s1[0], s2[0]), min(s1[1], s2[1]))
    length = interval[1] - interval[0]

    if length < 0:
        return "NO"
    if is_prime(length):
        return "YES"
    else:
        return "NO"
```

The approach uses a simple algorithm for checking prime numbers, embodied in the `is_prime` function. It iterates from 2 up to the square root of the checked number, checking for divisibility. If the number is divisible by any integer in this range it is not prime. The `intersection` function converts the interval pair to a tuple, calculates the difference between the two extremes, and then checks if the length is prime. If the length is non-negative and prime, the function returns "YES"; otherwise, it returns "NO". 

To handle the edge case where the intervals do not intersect at all, we can simply check if the intervals' minimum and maximum values are less than each other, and return "NO" if so. This is handled in the above code. 

Here's how it would be used:
```python
# Test the function
print(intersection((1, 2), (2, 3)))  # Output: "NO"
print(intersection((-1, 1), (0, 4)))  # Output: "NO"
print(intersection((-3, -1), (-5, 5)))  # Output: "YES"
``` 

This code encapsulates the logic needed to solve the problem in a clear and efficient manner, allowing for easy testing and usage.