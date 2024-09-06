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
    s = max(s1[0], s2[0]) - min(s1[0], s2[0]) + 1
    if s1[1] < s2[1]:
        s = max(s, s1[1] - s2[0] + 1)
    elif s2[1] < s1[1]:
        s = max(s, s2[1] - s1[0] + 1)
    if is_prime(s):
        return "YES"
    else:
        return "NO"

# Test cases
tests = [
    ([1, 2], [2, 3], "NO"),
    ([-1, 1], [0, 4], "NO"),
    ([-3, -1], [-5, 5], "YES"),
]

for test in tests:
    assert intersection(*test[0]) == test[1]
```

The `is_prime` function is used to determine if a given number is prime. This function uses a combination of small prime numbers (up to 3) and the `6k ± 1` theorem to efficiently check if a number is prime. If the number is greater than 3 and can be divided by neither 2 nor 3, it iterates through numbers of the form `6k ± 1` (which are also prime) to check for divisibility. If the number is divisible by any prime number in this range, it returns `False`. If it reaches the end of the range without finding a divisor, it returns `True`.

The `intersection` function calculates the length of the intersection of two intervals, and then calls `is_prime` to determine if this length is prime. If the intervals do not intersect or the intersection length is not prime, it returns "NO". If the intersection length is prime, it returns "YES".