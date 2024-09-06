```python
def is_prime(n):
    """Check whether a given number is prime."""
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

# Test the function
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

In this code, we define a function `is_prime` that takes an integer `n` as input and checks whether it's prime or not. The function implements the basic primality checks, including divisibility by 2 and 3, and other prime checking rules. The function also uses the optimized approach with looping to improve efficiency for larger numbers. 

This function can be used to quickly determine whether a given number is prime or not, which can be helpful in various applications involving prime numbers.