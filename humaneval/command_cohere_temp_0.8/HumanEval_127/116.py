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
    elif is_prime(st - s1[0] + s2[0]) and is_prime(en - st):
        return "YES"
    else:
        return "NO"
```

The approach uses a simple algorithm to determine if the intersection's length is prime. The function `is_prime` determines whether a given integer is prime. It returns 'YES' if the intersection is prime and 'NO' if it is not. It returns 'NO' if the intervals do not overlap. To determine if the result is prime, it checks all divisors from 2 to the square root of the length and checks whether the number is divisible by any of them. The `intersection` function checks for an overlap and calls `is_prime` on the intersection's length.