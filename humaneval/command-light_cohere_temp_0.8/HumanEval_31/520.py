```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function with markdown code input
test_is_prime = is_prime  # Store the function call
test_is_prime(6)  # Should return False
test_is_prime(101)  # Should return True
test_is_prime(11)  # Should return True
test_is_prime(13441)  # Should return True
test_is_prime(61)  # Should return True
test_is_prime(4)  # Should return False
test_is_prime(1)  # Should return False
``` 

This Python code defines a function `is_prime` that checks whether a given number is a prime or not. The function iterates from 2 to the square root of the number, and checks for divisibility. It returns `True` if the is a prime and `False` otherwise. The code then provides test cases for the function, which should pass the tests successfully. 

Therefore, the provided code appears to be correct and effectively checks whether a given number is prime or not.