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
    smin = max(s1[0], s2[0])
    smax = min(s1[1], s2[1])
    if smin > smax:
        return "NO"
    else:
        diff = smax - smin
        if is_prime(diff):
            return "YES"
        else:
            return "NO"
```

The function `intersection()` takes two intervals as input, and returns "YES" if the length of the intersection is a prime number, and "NO" otherwise. The function checks if the difference between the max and min values of the intersection is a prime number using the `is_prime()` function. The `is_prime()` function checks if a given number is prime using the trial division method. It iterates through numbers from 5 to the square root of the number and checks for divisibility. If the number is divisible by any integer within this range, it's not a prime. Otherwise, it returns True.