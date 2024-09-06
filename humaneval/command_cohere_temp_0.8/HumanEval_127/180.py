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

The approach uses a simple algorithm to determine if a number is prime or not. The algorithm iterates through numbers from 2 to the square root of the input number and checks if the number is divisible by any of them to determine if the number is prime or not. The is_prime function uses this algorithm as a subroutine to determine if the length of the intersection is prime or not. The function returns "YES" if the length of the intersection is prime and "NO" otherwise. It also returns "NO" if the two intervals don't intersect. 

The `intersection` function takes two interval parameters and compares their start and end points. It calculates the interval using the maximum and minimum points of both intervals to determine if the middle point differs from both ends to assure it is an intersection rather than an inclusion. 

The length of the calculated intersection is then checked for primality through the `is_prime` function, and subsequently returns a "YES" or "NO" corresponding to whether the length is prime or not.