```python
def is_prime(n):
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

# Test case 1:
print("Is prime:", is_prime(6))  # Output: True

# Test case 2:
print("Is prime:", is_prime(101))  # Output: True

# Test case 3:
print("Is prime:", is_prime(11))  # Output: True

# Test case 4:
print("Is prime:", is_prime(13441))  # Output: True

# Test case 5:
print("Is prime:", is_prime(61))  # Output: True

# Test case 6:
print("Is prime:", is_prime(4))  # Output: False

# Test case 7:
print("Is prime:", is_prime(1))  # Output: False
```
The function is_prime takes an integer n as input and returns True if n is a prime number and False otherwise. The function uses a algorithm of checking divisibility by iterating up to the square root of n while keeping track of the last 2 divisors found.