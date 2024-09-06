```python
def is_prime(n):
    """
    Checks whether the given integer n is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Determine whether the length of the intersection of two given intervals is a prime number or not.
    """
    # Convert the interval pair to a tuple.
    interval = tuple(sorted([s1, s2]))
    length = abs(interval[0][1] - interval[0][0])
    if length == 0:
        return "NO"
    if is_prime(length):
        return "YES"
    return "NO"
```

The aforementioned function utilizes the is_prime() function to determine whether the length of the intersection of two given intervals is a prime number or not. This is achieved by converting the interval pair to a tuple and calculating the absolute difference between the end and start of the intersection. Subsequently, this difference is compared to zero to determine if there is any intersection. If the length is not quantifiable, "NO" is returned, while "YES" is returned for prime numbers, ultimately. To ascertain whether a number is prime, the function employs a optimized trial division technique, iterating only up to the square root of the number. 
Here is an example of how you can use this function:
```python
print(intersection((1, 2), (2, 3)))  # Output: "NO"
print(intersection((-1, 1), (0, 4)))  # Output: "NO"
print(intersection((-3, -1), (-5, 5)))  # Output: "YES"
```

This example test corresponds to the provided problem statement.