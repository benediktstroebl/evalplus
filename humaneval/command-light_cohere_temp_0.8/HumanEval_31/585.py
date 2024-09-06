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
def test_prime(n):
    return is_prime(n)

# Test suite to run the function
print("Test suite:")
print("Is 6 a prime?", test_prime(6))  # Output: False
print("Is 101 a prime?", test_prime(101))  # Output: True
print("Is 11 a prime?", test_prime(11))  # Output: True
print("Is 13441 a prime?", test_prime(13441))  # Output: True
print("Is 61 a prime?", test_prime(61))  # Output: True
print("Is 4 a prime?", test_prime(4))  # Output: False
print("Is 1 a prime?", test_prime(1))  # Output: False
```
This Python function `is_prime` determines whether a given number is a prime, returning `True` if the number is prime and `False` otherwise. The function begins by establishing a condition for prime numbers: if the number is less than or equal to 1, it is not prime. 

Next, the function examines the number's relationship to 2 and 3. It returns `False` if the number is even or an odd multiple of 3. The function then sets up an loop that iterates up to the square root of the number, testing for divisibility by each prime number. 

The function returns `True` if the number is divisible by any of these prime numbers, indicating that the number is not prime. The test function `test_prime` is used to test the `is_prime` function, and the test suite contains a collection of test cases. The `test_prime` function returns `True` for the test cases that are prime and `False` otherwise, confirming that the `is_prime` function is working correctly.