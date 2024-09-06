```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def intersection(s1, s2):
    st, ed = max(s1[0], s2[0]), min(s1[1], s2[1])
    if st > ed:
        return "NO"
    elif is_prime(st-ed+1):
        return "YES"
    else:
        return "NO"

# Test cases
assert intersection((1, 2), (2, 3)) == "NO"
assert intersection((-1, 1), (0, 4)) == "NO"
assert intersection((-3, -1), (-5, 5)) == "YES"
```

The approach uses a simple optimization of checking only the length of the intersection of the two intervals, instead of checking every possible combination of numbers, to determine if it's prime. If the length is less than 2, it's not prime. If it's 2, it's prime. For lengths more than 2, it iterates through numbers from 3 and above, optimizing by incrementing by 2 each time, checking if the number divides the length. If it does, it's not prime, otherwise, it is.