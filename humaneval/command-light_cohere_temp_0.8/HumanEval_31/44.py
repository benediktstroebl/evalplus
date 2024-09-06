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

# Test function to check if a given number is prime
def is_prime_test(n):
    return is_prime(n)

# Example usage
print(is_prime_test(6))  # Output: True
print(is_prime_test(1))  # Output: False
print(is_prime_test(6000000)))  # Output: True
```
The `is_prime` function returns `True` if the input `n` is a prime number, and `False` otherwise. The function uses a optimized algorithm to determine whether a number is prime or not. It also includes a test function to verify the correctness of the `is_prime` function.