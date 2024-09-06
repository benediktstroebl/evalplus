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

The approach uses a simple algorithm to determine if a number is prime or not. Then, the algorithm checks if the intersection interval is a prime number using the `is_prime` function. 

The `intersection` function maximizes the start interval and minimizes the end interval between the two input intervals. It then checks whether the length of the intersection is a prime number or not. If the length is prime, it returns `YES`, otherwise, it returns `NO`. Also, if the intersection length is less than or equal to 0, it means no intersection exists, hence it returns `NO`.