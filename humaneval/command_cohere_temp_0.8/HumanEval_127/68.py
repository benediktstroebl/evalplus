```python
def is_prime(n):
    """
    Checks if a number is prime
    Args:
        n (int): Number to check if prime
    Returns:
        bool: True if n is prime, otherwise False
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Check if the intersection of two intervals is a prime number
    Args:
        s1 (tuple): First interval (start, end)
        s2 (tuple): Second interval (start, end)
    Returns:
        str: "YES" if intersection is prime, otherwise "NO"
    """
    if not (s1[0] <= s2[1] and s2[0] <= s1[1]):
        return "NO"
    intersection_start = max(s1[0], s2[0])
    intersection_end = min(s1[1], s2[1])
    intersection_length = intersection_end - intersection_start
    if is_prime(intersection_length):
        return "YES"
    return "NO"
```

The function utilizes the `is_prime` helper function to determine if the length of the intersection of two intervals is a prime number or not. 

The `is_prime` function checks if a number is less than or equal to 1, it returns False immediately as such a number can't be prime. It then goes through a loop starting from 2 and going up to the square root of the number n, if at any point n divides evenly with any number in that range, it returns False immediately because primes greater than 2 are not divisible by any other number lesser than or equal to its square root. If the for loop completes without returning False, the number is prime. 

The `intersection` function first checks if the two intervals don't intersect at all by comparing the start of the first interval to the end of the second one and the other way around, if this isn't the case it proceeds to calculate the intersection by taking the maximum of the starts of both intervals and the minimum of the ends of both intervals to figure out the start and end of the intersection. It then calculates the length of the intersection and calls the `is_prime` function to check if the length of the intersection is prime. 

The code can be verified for correctness with the following tests:
```python
# Testing the is_prime function
print(is_prime(0))        # Output: False
print(is_prime(1))        # Output: False
print(is_prime(2))        # Output: True
print(is_prime(3))        # Output: True
print(is_prime(4))        # Output: False
print(is_prime(5))        # Output: True
print(is_prime(6))        # Output: False
print(is_prime(101))      # Output: True

# Testing the intersection function
print(intersection((1, 2), (2, 3)))        # Output: "NO"
print(intersection((-1, 1), (0, 4)))        # Output: "NO"
print(intersection((-3, -1), (-5, 5)))     # Output: "YES"
``` 

The `is_prime` function has a time complexity of O(sqrt(n)) where n is the number to be checked for primality and the `intersection`