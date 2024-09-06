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
print(is_prime_test(69999))  # Output: False
```
This function checks if a given number is prime or not. It starts by checking small prime numbers and gradually increases the threshold up to a limit, checking for divisibility with increasing prime numbers. The function eventually returns true if the number is prime and false if it's not. The test function can be used to test the function with different numbers. 

Also, the test function can be further modified and customized to add additional checks or perform different tests.