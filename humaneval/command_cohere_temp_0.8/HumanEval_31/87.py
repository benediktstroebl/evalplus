```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
``` 

This function adheres to the problem statement, returning `True` for prime numbers and `False` otherwise. It extensively utilizes the modulo operator (`%`) to determine whether the number is divisible by any integer between 2 and the number itself. This is a crucial characteristic of prime numbers - they are only divisible by 1 and themselves. Consequently, the function excels in exposing the underlying primality of numbers.

## Testing

To fully appreciate the robustness and accuracy of the `is_prime` function, it is essential to subject it to a wide array of tests that encompass a variety of prime and non-prime numbers. This systematic approach helps to validate its design and ensures its reliability in identifying prime numbers with consistency.

Here's a set of test cases to demonstrate the function:
```python
# Test for prime numbers
assert is_prime(101) == True
assert is_prime(11) == True
assert is_prime(13441) == True
assert is_prime(61) == True

# Test for non-prime numbers
assert is_prime(6) == False
assert is_prime(4) == False
assert is_prime(1) == False
```

These test cases effectively cover both prime and non-prime numbers, thereby underscoring the ability of the function to accurately categorize numbers according to their primality. Furthermore, a comprehensive test suite should include a diverse range of numbers, including borderline cases and those potentially encountering unexpected behaviors. This approach ensures a robust primality test function.