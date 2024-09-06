Here is a self-contained Python script that solves the problem of determining whether a given number is a prime or not, and passes the tests you have provided:
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

# Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False)
```

This script defines the function `is_prime` that checks whether a given number is prime or not. It uses some basic heur strategies, such as checking divisibility by 2 and 3 and then checking for divisibility by numbers forming the square of the root of the number. 
The test cases in the script are then passed to the `is_prime` function to verify its correctness.