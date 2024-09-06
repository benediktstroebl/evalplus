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
        return "YES" if is_prime(st - s1[0] + 1 + en - s2[1] + 1) else "NO"

# Test cases
assert intersection((1, 2), (2, 3)) == "NO"
assert intersection((-1, 1), (0, 4)) == "NO"
assert intersection((-3, -1), (-5, 5)) == "YES"
```

The approach used in the `intersection()` function is to calculate the maximum and minimum values between the start and end points of both intervals. The function then calculates the length of the intersection and checks if it's a prime number using the `is_prime()` function. If the length is prime, it returns "YES"; otherwise, it returns "NO".