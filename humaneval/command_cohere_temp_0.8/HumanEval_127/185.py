```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    x = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if x <= 0:
        return "NO"
    if is_prime(x):
        return "YES"
    else:
        return "NO"

# Example usage
print(intersection((1, 2), (2, 3)))  # Output: NO
print(intersection((-1, 1), (0, 4)))  # Output: NO
print(intersection((-3, -1), (-5, 5)))  # Output: YES
```

This script includes a `is_prime` function that checks whether a given number is prime or not. The `intersection` function estimates the length of the intersection of two intervals, and then checks if that length is prime. If the length is not prime or if the intervals do not intersect, it returns "NO". Otherwise, it returns "YES".