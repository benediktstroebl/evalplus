```python
def is_prime(n):
    """
    A recursive function to check if a number is prime. 
    Returns True if n is prime, else False.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This code defines a function `is_prime` that checks if a given number `n` is prime. 

It uses a combination of conditions and a recursive approach to determine whether a number is prime or not. 

The function initially handles the cases where n is less than or equal to 1 and returns `False` since these are not prime. Then, it handles the cases where n is of the form 6k + 2 or 6k - 1, where k is an integer, and returns `False` since these numbers are multiples of 6. 

Finally, the function uses a while loop to check for divisibility up to the square root of n, returning `True` if the condition for divisibility is not met. 

This function can be effectively used to check for primality in various numbers and pass the test of being a prime function.