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

# Example usage
print(intersection((1, 2), (2, 3)))
print(intersection((-1, 1), (0, 4)))
print(intersection((-3, -1), (-5, 5)))
```

The approach uses a well-known primality testing algorithm called the `6k ± 1` rule, which is an optimization of trial division for checking primality. The function `is_prime` implements this algorithm to efficiently determine if a given number is prime or not. 

The `intersection` function calculates the endpoints of the intersection of two intervals, and then calls `is_prime` to test the length of the intersection range. If the length is prime, it returns "YES"; otherwise, it returns "NO".