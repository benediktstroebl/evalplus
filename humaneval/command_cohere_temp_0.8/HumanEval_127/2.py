```python
def is_prime(n):
    """
    Checks if a number is prime
    Args:
        n (int): number to check if prime
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
    Check if the intersection of two intervals is a prime number
    Args:
        s1 (tuple): first interval (start, end)
        s2 (tuple): second interval (start, end)
    Returns:
        str: "YES" if intersection is prime, otherwise "NO"
    """
    if not (s1[0] <= s2[1] and s1[1] >= s2[0]):
        return "NO"
    intersection_start = max(s1[0], s2[0])
    intersection_end = min(s1[1], s2[1])
    intersection_length = intersection_end - intersection_start
    if is_prime(intersection_length):
        return "YES"
    return "NO"
```

The function utilizes the `is_prime` helper function to determine if the length of the intersection of two intervals is a prime number or not. The `is_prime` function checks if a number is less than or equal to 1, it returns False; if the number is greater than 1, it checks if there are any divisors between 2 and the square root of the number, if there are no divisors, it returns True. 

The `intersection` function first checks if the two intervals overlap, if they don't, it returns "NO". If they do, it calculates the length of the intersection and then passes it to the `is_prime` function to determine if the length of the intersection is prime. If it is prime, it returns "YES"; otherwise, it returns "NO". 

The expected complexity of the `intersection` function is O(1) due to the absence of recursive calls and iteration, whereas the complexity of the `is_prime` function is O(sqrt(n)) due to the loop ranging from 2 to int(n**0.5) + 1.