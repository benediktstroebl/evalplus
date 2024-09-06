```python
def is_prime(n):
    """
    Checks if a number is prime
    Args:
        n (int): number to check
    Returns:
        bool: True if n is prime, otherwise False
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Check if the intersection of two intervals is prime
    Args:
        s1 (tuple): first interval tuple (start, end)
        s2 (tuple): second interval tuple (start, end)
    Returns:
        str: "YES" if the intersection is prime, otherwise "NO"
    """
    if not (s1[0] <= s2[1] and s1[1] >= s2[0]):
        return "NO"
    else:
        intersect_start = max(s1[0], s2[0])
        intersect_end = min(s1[1], s2[1])
        intersect_len = intersect_end - intersect_start
        if is_prime(intersect_len):
            return "YES"
        else:
            return "NO"
```
The function uses a separate function, `is_prime`, to quickly check if a number is prime. The function iterates through numbers from 2 to the square root of the number and checks for divisibility. If the number is divisible by any integer in this range, it is not prime. If it's not divisible by any number in this range or if the number is less than or equal to 1, the number is prime. 

The `intersection` function checks if the intervals overlap using the `<=` and `>=` operators. If the intervals don't overlap, it returns "NO". Then, it calculates the length of the intersection and passes it to the `is_prime` function to determine if the length of the intersection is prime.

Overall, this code efficiently and accurately determines if the length of the intersection of two intervals is a prime number.