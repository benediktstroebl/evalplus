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

# Test function to check if a number is prime
def is_prime_test(n):
    return is_prime(n)

# Test cases
print(is_prime_test(6))  # Output: False
print(is_prime_test(101))  # Output: True
print(is_prime_test(11))  # Output: True
print(is_prime_test(13441))  # Output: True
print(is_prime_test(61))  # Output: True
print(is_prime_test(4))  # Output: False
print(is_prime_test(1))  # Output: False
```
The function `is_prime` checks if a given number is prime or not. The function uses the simple optimizations to quickly rule out certain numbers, and then uses a basic iterative algorithm to check divisibility up to the square root of the number. The test function `is_prime_test` uses the `is_prime` function to test if a number is prime or not. 
This self-contained Python script solves the problem of checking if a given number is prime and passes all the corresponding tests.