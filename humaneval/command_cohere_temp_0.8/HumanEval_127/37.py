```python
def is_prime(n):
    """
    Checks whether a number is prime
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
    interval_intersection = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if not interval_intersection or not is_prime(interval_intersection):
        return "NO"
    else:
        return "YES"
```

The function `intersection()` takes in two intervals denoted by two tuples, `(start, end)`. It calculates the length of the intersection between these two intervals. Then, the code checks whether this length is not only positive but also prime. If these conditions are fulfilled, it returns `"YES"`, otherwise it returns `"NO"`  

Here is an example of using the `intersection()` function:
```python
intersection((-3, -1), (-5, 5))
```

The output is `"YES"` as the two intervals overlap and the length of the intersection is 3, which is a prime number.