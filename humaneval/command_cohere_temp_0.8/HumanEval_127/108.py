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
```

The approach uses a simple algorithm to check if the intersection length is prime. The function `is_prime` checks if a given number is prime or not. The function uses several conditional checks to reduce the iterations. The main function `intersection` takes two intervals as input and returns "YES" if the length of the intersection is prime, "NO" if the length is not prime, and the intervals don't overlap return "NO". The overall time complexity of the program is O(L), where L is the length of the intersection of the given intervals. This is the best time complexity we can achieve for this problem.