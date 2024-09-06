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

This code defines a function `intersection()` that takes in two intervals represented as tuples and determines if the length of the intersection of these intervals is a prime number. The code also includes the `is_prime()` function to check if a given number is prime. 

The `intersection()` function first calculates the start and end points of the intersection of the two intervals using max and min functions. If the resulting interval is empty (`st > en`), it returns "NO." Otherwise, it calculates the length of the intersection and checks if this length is prime using the `is_prime()` function. If the length is prime, it returns "YES"; otherwise, it returns "NO."