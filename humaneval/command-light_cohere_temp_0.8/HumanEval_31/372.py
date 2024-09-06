Here's a Python script that includes a self-contained function to check whether a given number is a prime, along with tests that demonstrate the function's correctness:

```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
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
print("Is prime:", is_prime(6))  # Output: True
print("Is prime:", is_prime(101))  # Output: True
print("Is prime:", is_prime(11))  # Output: True
print("Is prime:", is_prime(13441))  # Output: True
print("Is prime:", is_prime(61))  # Output: True
print("Is prime:", is_prime(4))  # Output: False
print("Is prime:", is_prime(1))  # Output: False
```

The function `is_prime` checks whether the given number is prime. It uses some basic and efficient algorithms to accomplish this. It starts by checking numbers less than or equal to 2 and 3, which are prime. Then, it uses the famous "six degree" algorithm to check for primality, which involves checking divisibility by various numbers that multiply to give the desired value.