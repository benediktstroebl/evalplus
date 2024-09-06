```python
def is_prime(n):
    """
    Checks if a number is prime
    """
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
    """
    Determine if the intersection of two intervals is a prime number
    """
    start = max(s1[0], s2[0])
    end = min(s1[1], s2[1])
    if start > end:
        return "NO"
    length = end - start + 1
    if is_prime(length):
        return "YES"
    else:
        return "NO"
```
The approach used by the provided Python script is:
- The `is_prime` function is used to determine if a number is prime. This function uses a mix of small prime numbers (`2`, `3`) in its checks and performs trial divisions by numbers starting from `5` up to the square root of the number. This is an efficient primality test.
- The `intersection` function calculates the intersection of two intervals, and then calls `is_prime` to check if the length of the intersection is prime.

The script offers an elegant solution that perfectly fits the given problem. It's both concise and efficient in its use of primality testing, making it a great demonstration of Python's expressive power for solving coding challenges.