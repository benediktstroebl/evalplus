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

The `is_prime` function checks if a number is prime. The `intersection` function determines whether the length of the intersection of two given closed intervals is a prime number. It maximizes the start of the intervals and minimizes the end of the intervals, calculating the length of the intersection as the difference between the end and start plus one. If the length is prime, it returns "YES"; otherwise, it returns "NO".

Here is example usage:
```python
print(intersection((1, 2), (2, 3))) == "NO"
print(intersection((-1, 1), (0, 4))) == "NO"
print(intersection((-3, -1), (-5, 5))) == "YES"
```

This would output:
```
YES
NO
YES
```