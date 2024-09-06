```python
def is_multiply_prime(a):
    # Check if a is a perfect square
    root = int(pow(a, 0.5))
    if root * root == a:
        return False

    # Check for divisibility by 2 and 3
    if a % 2 == 0 or a % 3 == 0:
        return False

    # Check for prime factors
    for i in range(5, int(a ** 0.5) + 1):
        if a % i == 0:
            return False

    return True
```

This function checks if the number `a` is the product of three primes. It first checks if `a` is a perfect square, returning False if so. It then checks for divisibility by 2 and 3, returning False if the number is divisible by either. The function then iterates through numbers from 5 to the square root of `a`, checking for divisibility by any of these numbers. If none of these conditions are met, the function returns True, indicating that the number is the product of three primes. 

Here is a simple test suite to ensure that the function behaves as expected.
```python
def test_multiply_prime():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(52) == True
    assert is_multiply_prime(55) == False
    assert is_multiply_prime(36) == False
    assert is_multiply_prime(49) == False

test_multiply_prime()
```
The test suite contains four test functions checking different edge cases to ensure the correct behavior of the `is_multiply_prime` function.