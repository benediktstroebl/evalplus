```python
def is_prime(n):
    """
    Checks whether a number is prime
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
    Determine whether the length of intersection of two given closed intervals is prime.
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

The script employs a simple approach where it determines the maximum and minimum points of the intersection and then calculates its length. Subsequently, it utilizes a primality testing function to determine if the length is prime. Lastly, it returns a "YES" or "NO" accordingly. 
If you would like to include additional tests, feel free to do so and provide them in a code block with the description "**[input/output]**" as you did originally. Ex: ```python
# [input/output]
test_cases = [
    ((1, 2), (2, 3), "NO"),
    ((-1, 1), (0, 4), "NO"),
    ((-3, -1), (-5, 5), "YES"),
    ((-10, -5), (0, 10), "YES"),
    ((2, 3), (5, 7), "NO")
]
```