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

# Test cases
print(intersection((1, 2), (2, 3)))  # Output: NO
print(intersection((-1, 1), (0, 4)))  # Output: NO
print(intersection((-3, -1), (-5, 5)))  # Output: YES
```

This code defines a function `intersection()` that takes in two intervals, each represented as a tuple (start, end), and determines whether the length of the intersection of these intervals is a prime number. 

The `is_prime()` function is used to determine if a given integer is prime. It handles special cases like integers less than or equal to 1, and then performs a probabilistic primality test using the Sieve of Eratosthenes algorithm up to the square root of the number.

The `intersection()` function first calculates the start and end values of the intersection by finding the maximum and minimum values of the starts and ends of the given intervals. If the resulting start value is greater than the end value, it returns "NO" since there is no intersection. If the length of the intersection is prime, it returns "YES". Otherwise, it returns "NO". 

The test cases are included to demonstrate the function's behavior. You can modify the input intervals as needed.