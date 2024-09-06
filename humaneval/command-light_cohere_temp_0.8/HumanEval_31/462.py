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

# Test cases
print(is_prime_test(6))  # Output: False
print(is_prime_test(101))  # Output: True
print(is_prime_test(11))  # Output: True
print(is_prime_test(13441))  # Output: True
print(is_prime_test(61))  # Output: True
print(is_prime_test(4))  # Output: False
print(is_prime_test(1))  # Output: False
```
This code defines a function `is_prime` that checks if a given number is prime. The function uses a `if...else` statement to check different cases of divisibility. The function also uses a `while...else` statement to iterate up to the square root of the number and check for divisibility up to that value. The function also uses a `return` statement to return `True` if the number is prime and `False` otherwise. 

The code also defines a test function `is_prime_test` that calls the `is_prime` function with a given number and returns the result. The test cases are also calling the `is_prime_test` function with a few test numbers and printing the output.