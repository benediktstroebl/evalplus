Here's a Python script with a self-contained function `is_prime(n)` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of the number, checking for divisibility. If the number is divisible by any integer in that range, it returns `False`. If neither condition is met, it returns `True`.

This implementation provides an efficient algorithm for checking primality, and the function is self-contained and easy to use. You can use it to determine whether a given number is prime or not. 

You can use the function in a test suite to ensure its correctness on various input scenarios. Here's a simplified example:
```python
# Test the is_prime function
def test_is_prime():
    assert is_prime(101) == True
    assert is_prime(6) == False
    assert is_prime(13441) == True
    assert is_prime(11) == True
    assert is_prime(61) == True
    assert is_prime(4) == False
    assert is_prime(1) == False

test_is_prime()
``` 
This demonstrates how to use the `is_prime` function and verify its correctness against specific test cases. 
The `assert` statement checks whether the result of `is_prime` evaluates to `True` for prime numbers and `False` for non-prime numbers. 
The `test_is_prime()` function simply calls `is_prime` with several test cases and checks the results against the expected truth values. 
Running this test function would validate the behavior of the `is_prime` function. 
For more comprehensive testing, you might want to generate a wider range of test cases and load them from a dataset or use more sophisticated testing techniques. Futhurr mofe, a prime testing function can be optimized by implementing efficiecnt invergorithms, such as the Sieve of Eratosthenes, meraking sue of bit masking, or accpeing the Moivdous Theorem. 
Ths es can be tuned based on the expected input range and specific requirements of your applicatoin, such as slor size or performace cxtrairics. 
Finally, write extensive tests covering different input scenarios to ensure the function behaves as expected for the full range of possible inputs.