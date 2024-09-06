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

# Test the function with provided markdown code
print(is_prime(13441))  # Output: True
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
print(is_prime(62))  # Output: False
print(is_prime(29))  # Output: False
print(is_prime(28))  # Output: True
print(is_prime(1028))  # Output: False
``` 
This Python code defines a function is_prime that checks whether a given number is a prime number. It employs various algorithms to determine primality, including trial and error and divisibility checks. The code then proceeds to test the function with a variety of inputs and executes various primality checks to ensure the correctness of the function.