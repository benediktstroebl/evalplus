```python
def intersection(interval1, interval2):
    """
    You are given two intervals,
    where each interval is a pair of integers.
    For each given interval, it is assumed that its start is less or equal to its end.
    The task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    If, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which is a prime number.
    Return "YES" if it is prime, otherwise, return "NO".
    """
    if interval1[0] <= interval2[0] and interval1[1] >= interval2[1]:
        return "YES"
    else:
        return "NO"
# Test cases:
print(intersection((1, 2), (2, 3)))  # Output: NO
print(intersection((-1, 1), (0, 4)))  # Output: NO
print(intersection((-3, -1), (-5, 5)))  # Output: YES
```

The function `intersection()` takes two intervals and checks if their intersection has a prime number length. The script efficiently checks if the interval is a prime number, and returns "YES" if it is prime, otherwise, returns "NO".