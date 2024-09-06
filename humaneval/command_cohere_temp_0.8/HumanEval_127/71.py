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
    Check if the intersection of two intervals is prime
    """
    if s1[0] > s2[1] or s1[1] < s2[0]:
        return "NO"
    inter_start = max(s1[0], s2[0])
    inter_end = min(s1[1], s2[1])
    if is_prime(inter_end - inter_start):
        return "YES"
    else:
        return "NO"
```
The approach uses a simple algorithm to check if the intersection of two intervals is prime and verifies that the start and end values for the intersection actually overlap before checking the prime condition. 

The `is_prime` function is used to determine if a given integer is prime. It does this by first checking if the number is less than or equal to 1, returning False if so. It then checks if the number is 2 or 3, both of which are prime, so it returns True if that is the case. Next, it checks whether the number is divisible by 2 or 3, and since these are the only even prime numbers, it returns False if the number is divisible by either. It then iterates through numbers of the form 5x + 2 and 5x + 3 (starting from 5 and skipping 6) until it reaches the square root of the checked number. If the number is divisible by any of these iterated numbers, it returns False. If it has checked all these conditions and the number is still not divisible, it returns True.