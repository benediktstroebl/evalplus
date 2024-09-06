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

The approach uses a simple algorithm to determine if the intersection of two intervals is a prime number. 

The `is_prime` function checks if a given number is prime using a combination of conditions and optimizations, such as checking divisibility by 2 and 3, then checking in increments of 6 until the square root of the number. 

The `intersection` function first calculates the maximum and minimum values between the two intervals, checking if the resulting interval is empty. If the interval is not empty, it proceeds to check if the length of the intersection is prime using the `is_prime` function. If it is prime, it returns "YES"; otherwise, it returns "NO". 

This approach takes advantage of the properties of prime numbers and interval operations, resulting in an efficient solution.