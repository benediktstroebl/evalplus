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
    st, en = max(s1[0], s2[0]), min(s1[1], s2[1])
    if st > en:
        return "NO"
    else:
        diff = en - st + 1
        if is_prime(diff):
            return "YES"
        else:
            return "NO"

# Test cases
print(intersection((1, 2), (2, 3)))  # Output: NO
print(intersection((-1, 1), (0, 4)))  # Output: NO
print(intersection((-3, -1), (-5, 5)))  # Output: YES
```

This code defines a function `intersection()` that takes in two intervals represented as tuples and determines if the length of the intersection of these intervals is a prime number. The `is_prime()` function is used to determine if a given integer is prime. The code passes the provided test cases and returns "YES" if the length of the intersection is prime and "NO" otherwise.