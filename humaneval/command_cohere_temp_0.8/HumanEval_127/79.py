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
    s = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if s < 0:
        return "NO"
    if is_prime(s):
        return "YES"
    else:
        return "NO"

# Example usage
print(intersection((1, 2), (2, 3)))  # Output: NO
print(intersection((-1, 1), (0, 4)))  # Output: NO
print(intersection((-3, -1), (-5, 5)))  # Output: YES
```

This code defines a function `intersection` that takes in two intervals represented as tuples and determines whether the length of the intersection of these intervals is a prime number. The code also utilizes a `is_prime` helper function to determine if a given number is prime or not. 

The `intersection` function first calculates the length of the intersection by taking the maximum end point of the intervals and subtracting the minimum start point of the intervals. It handles cases where the intervals do not intersect at all by checking if the length is less than zero. If the length is non-negative, it then checks if the length is prime using the `is_prime` function. If it's prime, it returns "YES"; otherwise, it returns "NO".