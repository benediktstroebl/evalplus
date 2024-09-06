```python
def is_prime(n):
    """
    Checks whether a positive integer 'n' is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Checks whether the length of the intersection of two given intervals is a prime number or not.
    """
    x = min(s1[1], s2[1]) - max(s1[0], s2[0])
    if x < 0 or not is_prime(x):
        return "NO"
    else:
        return "YES"

# Test cases
assert intersection((0, 4), (1, 3)) == "NO"
assert intersection((-5, 0), (0, 4)) == "NO"
assert intersection((-3, -1), (-5, 5)) == "YES"
```

The `is_prime` function is used to determine if a given positive integer is prime. This function checks if the number is less than or equal to 1, it returns False; if the number is divisible by any integer between 2 and its square root, it returns False. If none of these conditions are met, it returns True. 

The `intersection` function calculates the length of the intersection of two given intervals, and checks if the length is prime. If the intervals don't intersect or the length of the intersection is not prime, it returns "NO". If the length of the intersection is prime, it returns "YES".

The test cases are meant to ensure the function `intersection` performs as expected based on the problem statement.