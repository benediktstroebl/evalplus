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

The `is_prime` function checks if a number is prime. It first checks if the given number is less or equal to 1, returning `False` if so. Then, it checks if the number is 2 or 3, both prime numbers, and returns `True` if so. Following this, the function checks if the number can be divided by 2 or 3, returning `False` if so. Finally, the function uses a while loop to check for divisibility by numbers of the form `i` and `i + 2`, where `i` starts as 5 and increases by 6 each iteration. If the number is divisible by any such number, or is equal to 1, the function returns `False`. If the while loop completes without finding a divisor, the function returns `True`. The `intersection` function finds the intersection of two intervals, defined as pairs of integers. It uses the `is_prime` function to check if the length of the intersection is prime. If the intervals don't intersect, it returns `NO`. If the length of the intersection is prime, it returns `YES`. Otherwise, it returns `NO`. 
This code is efficient and relatively optimized for this type of problem.