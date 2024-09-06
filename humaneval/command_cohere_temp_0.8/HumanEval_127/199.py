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
    start = max(s1[0], s2[0])
    end = min(s1[1], s2[1])
    if start > end:
        return "NO"
    length = end - start + 1
    if is_prime(length):
        return "YES"
    else:
        return "NO"
```

The `is_prime` function checks if a number is prime or not. It loops from 2 to the square root of the number and checks for divisibility. If the number is divisible by any integer within this range it returns `False`. If the number is not divisible by any integer within this range, it returns `True`. 

The `intersection` function calculates the intersection of two intervals, as explained in the problem statement. It calculates the exclusive intersection interval using the `max` and `min` functions and calculates its length. Then the length is checked against the `is_prime` function to determine if it's a prime number or not. 

The `intersection` function is self-contained and can be used to solve the problem as required.