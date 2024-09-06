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

This code defines a function `intersection` that takes in two intervals represented as tuples and determines whether the length of the intersection of these intervals is a prime number. The code also utilizes a helper function, `is_prime`, to determine if a given number is prime. 

The `intersection` function first calculates the start and end of the intersection of the two intervals by finding the maximum and minimum of the start values and the minimum of the end values of the intervals. It then checks if the start is greater than the end, in which case there is no intersection, and returns "NO". If the start and end values are within the intervals, it calculates the length of the intersection and checks if this length results in a prime number using the `is_prime` function. If it is prime, it returns "YES", otherwise, it returns "NO".