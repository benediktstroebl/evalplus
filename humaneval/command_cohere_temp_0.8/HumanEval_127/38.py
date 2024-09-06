```python
def is_prime(n):
    """
    Checks whether a positive integer is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Determine whether the length of the intersection of two closed intervals is prime
    """
    interval_intersection = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if not interval_intersection or not is_prime(interval_intersection):
        return "NO"
    else:
        return "YES"
```
The approach uses a simple primality test function, `is_prime`. The `intersection` function determines the length of the intersection of the intervals, checks if the intersection length is non-empty and then uses `is_prime` to test if the length is prime. 

#### Here is the separable primality test function: 
```python
def is_prime(n):
    """
    Checks whether a positive integer is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
``` 

This function takes int n as input and tests whether n is prime using a divisibility test. It loops from 2 to the square root of n and checks whether any number in that range divides evenly into n. If it finds any such number, it returns False, indicating that n is not prime. If it finishes the loop without finding any divisor, it returns True, indicating that n is prime. 

```python
def intersection(s1, s2):
    """
    Determine whether the length of the intersection of two closed intervals is prime
    """
    interval_intersection = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if not interval_intersection or not is_prime(interval_intersection):
        return "NO"
    else:
        return "YES"
``` 

This function takes two interval tuples s1 and s2 as input and returns a string indicating whether the intersection of the intervals is prime. It calculates the length of the intersection using the formula `interval_intersection = max(s1[1], s2[1]) - min(s1[0], s2[0])`. It then checks if the intersection length is non-empty and not prime, it returns "NO". If the length is non-empty and prime, it returns "YES". 

The function uses a primality test function, `is_prime`, to determine if the intersection length is prime. The `is_prime` function takes an integer as input and returns a boolean indicating whether the input is prime. 

Overall, the code returns "YES" if the intersection of the intervals is non-empty and prime, and it returns "NO" otherwise.