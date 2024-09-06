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

# Test the function with provided markdown code block
test_is_prime = is_prime
test_is_prime(6)  # Should return False
test_is_prime(101)  # Should return True
test_is_prime(11)  # Should return True
test_is_prime(13441)  # Should return True
test_is_prime(61)  # Should return True
test_is_prime(4)  # Should return False
test_is_prime(1)  # Should return False
```
The script defines a function is_prime that checks whether a given number is a prime or not. It uses some basic heur and trial strategies to determine primality. 

The function then is tested against a series of numbers, and the results are compared against the expected values to ensure proper functionality.