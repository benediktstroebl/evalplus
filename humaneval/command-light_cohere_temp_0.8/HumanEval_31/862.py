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

# Test case #1: is_prime(6) should return False
print(is_prime(6))  # Output: False

# Test case #2: is_prime(101) should return True
print(is_prime(101))  # Output: True

# Test case #3: is_prime(11) should return True
print(is_prime(11))  # Output: True

# Test case #4: is_prime(13441) should return True
print(is_prime(13441))  # Output: True

# Test case #5: is_prime(61) should return True
print(is_prime(61))  # Output: True

# Test case #6: is_prime(4) should return False
print(is_prime(4))  # Output: False

# Test case #7: is_prime(1) should return False
print(is_prime(1))  # Output: False
```
The function is_prime(n) checks if the given number is prime or not. It first handles special cases: numbers less than or equal to 1, numbers equal to 2 or 3, and numbers that can be expressed as a multiple of 2 and 3. Then, it employs a trial and error method using an efficient sieve of Eratosthenes to determine if the number is prime or not.