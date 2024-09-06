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
    Checks whether the intersection of two intervals is a prime number
    """
    if max(s1[1], s2[1]) < min(s1[0], s2[0]):
        return "NO"
    interval_length = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if is_prime(interval_length):
        return "YES"
    else: 
        return "NO"
```

The function relies on the `is_prime` helper function, which determines whether a given number is prime. This simplicity enables the `intersection` function to focus on the core logic of calculating the interval overlap and delegating the primality check to a purpose-built helper function. This organization makes the code more manageable and easier to understand, maintaining a logical division of responsibilities. 

The `intersection` function first determines whether the intervals overlap at all, discarding any non-intersecting scenarios right away. It then calculates the length of the intersection and passes this value to the `is_prime` function to determine whether the length is prime.