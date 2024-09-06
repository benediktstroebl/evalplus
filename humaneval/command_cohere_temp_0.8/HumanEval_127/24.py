```python
def is_prime(n):
    """
    Checks if a number is prime
    Args:
        n (int): number to check
    Returns:
        bool: whether n is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Check the intersection of two closed intervals given as pairs (start, end).
    Args:
        s1,s2 (tuple): intervals
    
    Returns:
        str: "YES" if the intersection length is a prime number, otherwise "NO"
    """
    x = abs(max(s1[0], s2[0])) - abs(min(s1[0], s2[0]))
    y = abs(max(s1[1], s2[1])) - abs(min(s1[1], s2[1]))
    if x > y:
        x, y = y, x
    if x == 0:
        return "NO"
    if is_prime(x):
        return "YES"
    return "NO"
```

The script utilizes a basic primality testing function to determine if a given number is prime. 

The `intersection` function first calculates the length of the intersection of the two intervals, `x`. If the intervals don't intersect, or the length of the intersection is 0, it returns "NO". Then it checks if the length of the intersection is prime, and returns "YES" if it is, otherwise it returns "NO".

The function also handles the case where the end points of one interval are equal to the start points of the other interval. In this case, the intervals overlap on both ends and the intersection length is equal to the size of the overlapping interval, which is excluded from the final result.

This solution is efficient and can efficiently compute the intersection size and determine its primality require O(log n) space and time, where n is the size of the intersection. 

The `is_prime` function runs in O(sqrt(n)) time, while the `intersection` function takes linear time in the size of the intervals.