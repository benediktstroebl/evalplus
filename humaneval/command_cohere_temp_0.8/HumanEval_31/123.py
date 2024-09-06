Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a number is prime or not. It first checks if the number is smaller than 2, returning false in this case. Then, it iterates from 2 up to the square root of the number `n`, checking if the number is divisible by any of these integers. If the number is divisible by any of them, it returns false; otherwise, it returns true.

Here is a snippet of tests to ensure the function works correctly:
```python
# Test case
def test_is_prime():
    assert is_prime(101) == True
    assert is_prime(6) == False
    assert is_prime(11) == True
    assert is_prime(13441) == True
    assert is_prime(61) == True
    assert is_prime(4) == False
    assert is_prime(1) == False
``` 

This test suite includes a variety of tests, from edge cases (e.g., handling numbers less than 2) to sporadic examples of prime and non-prime numbers. 

To run the test suite, you can use a testing framework like `pytest`. This way, you can confidently confirm the function's correctness and robustness against different scenarios.