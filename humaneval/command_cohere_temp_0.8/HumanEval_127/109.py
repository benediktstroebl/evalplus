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
    s1, s2 = min(s1), min(s2)
    e1, e2 = max(s1), max(s2)
    if s1 > e2 or s2 > e1:
        return "NO"
    length = e1 - s1 + 1
    return "YES" if is_prime(length) else "NO"
```

The approach uses a simple algorithm to determine if the generated number is prime or not. The algorithm checks divisibility by numbers of the form `6k ± 1` up to the square root of the number. The efficiency of the algorithm is O( √n ). Where n is the number to be checked for primality. 

The `intersection` function evaluates the intersection of two closed intervals specified by the pairs `(s1, s2)` and `(s1, e1)` respectively. It returns "YES" if the length of the intersection is a prime number, and "NO" otherwise. Also returns "NO" if the intervals don't intersect at all.