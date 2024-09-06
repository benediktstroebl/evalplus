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
    # Convert interval to integer interval
    start = max(s1[0], s2[0])
    end = min(s1[1], s2[1])
    
    # Check if there is an intersection
    if end < start:
        return "NO"
    
    length = end - start + 1
    if is_prime(length):
        return "YES"
    else:
        return "NO"
```

The `is_prime` function checks whether a given number n is prime or not. It iterates from 2 to n**0.5, checking whether n is divisible by any number in that range. If it is, it returns `False`. If it goes through the whole range without finding a divisor, it returns `True`. This check is fast for primality testing for large numbers.

The `intersection` function calculates the intersection of two intervals, converting them to start and end points, taking the maximum and minimum values of the start points and the start points themselves, respectively. 

It then checks if the resulting length is prime, and returns "YES" if so, or "NO" otherwise. If the intervals do not intersect, it returns "NO". This approach ensures that the intervals are treated as closed intervals, as specified in the problem statement.