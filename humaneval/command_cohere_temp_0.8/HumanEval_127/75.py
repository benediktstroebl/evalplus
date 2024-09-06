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
    if s == 0 or is_prime(s):
        return "YES"
    else:
        return "NO"
```

The approach uses a simple algorithm to determine if the intersection interval's length is prime. It also takes care of cases where intervals don't have any overlap or endpoints overlap, both of which would result in an empty intersection or not a prime intersection length respectively. The `is_prime` function is used from the [Prime Number Algorithm Problems](https://github.com/TheAlgorithms/Python/blob/main/Prime_Number_Algorithm_Problems.py) repository to check if a given number is prime.  This approach assumes that intervals are given in the format of `(start, end)`, which is the convention for closed intervals.