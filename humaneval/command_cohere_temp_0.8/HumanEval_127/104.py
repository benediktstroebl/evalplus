```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def intersection(s1, s2):
    st, en = max(s1[0], s2[0]), min(s1[1], s2[1])
    if st > en:
        return "NO"
    elif is_prime(st - en + 1):
        return "YES"
    else:
        return "NO"
```

The approach solves the problem by finding the length of the intersection of the two intervals using `max(s1[0], s2[0]); min(s1[1], s2[1])` and checks if it's prime using the `is_prime()` function. If the length is not prime, it returns "NO," and if it's prime, it returns "YES." Also, a prime-checking function is added to help validate the answer.