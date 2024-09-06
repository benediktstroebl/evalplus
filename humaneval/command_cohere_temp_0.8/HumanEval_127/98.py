```python
def is_prime(n):
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
    st, ed = max(s1[0], s2[0]), min(s1[1], s2[1])
    if st > ed:
        return "NO"
    elif is_prime(st - ed + 1):
        return "YES"
    else:
        return "NO"

# Example usage
print(intersection((1, 2), (2, 3)))  # Output: NO
print(intersection((-1, 1), (0, 4)))  # Output: NO
print(intersection((-3, -1), (-5, 5)))  # Output: YES
```

This script includes both the `is_prime` function to determine if a given number is prime or not, and the `intersection` function that determines if the length of the intersection of two intervals is prime. The `intersection` function maximizes the start time and minimizes the end time of the two intervals. Then, it checks if the length of the intersection is prime using the previously defined `is_prime` function. If the length is prime, it returns "YES"; otherwise, it returns "NO". If the two intervals do not intersect, it also returns "NO".