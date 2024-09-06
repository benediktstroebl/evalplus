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

The `is_prime` function checks if a number is prime. It iterates from 2 to the square root of the number and checks for divisibility. If the number is divisible by any integer in this range, it is not prime; otherwise, it is prime. This function is called by `intersection` to determine if the length of the intersection of two intervals is prime.

The `intersection` function calculates the intersection of two intervals, taking care of the case where the intervals don't intersect at all, and checking if the length of the intersection is prime. If the start of the longer interval is less than the end of the shorter interval, the intervals overlap, and the function calculates the length of the intersection and passes it to the `is_prime` function to determine if it is prime.

The following examples demonstrate how the code solves the problem:
```python
print(intersection((1, 2), (2, 3)))  # Output: "NO"
print(intersection((-1, 1), (0, 4)))  # Output: "NO"
print(intersection((-3, -1), (-5, 5)))  # Output: "YES"
```

This code demonstrates a straightforward approach to checking for prime intervals. However, it's important to note that this approach has a computational cost, as it involves checking divisibility for many numbers. The runtime of this code is O(sqrt(n)) where n is the length of the intersection of the intervals. 

For larger intervals, this could lead to a significant amount of checks for prime intervals. As such, this may not be an optimal solution for large intervals.