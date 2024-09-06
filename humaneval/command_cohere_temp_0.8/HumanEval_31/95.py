```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function is designed to determine whether a given number is prime. It begins by checking if the number is less than 2, returning False if so, as numbers less than 2 are not prime. The function then iterates through numbers from 2 up to the square root of the input number, checking whether the input number is divisible by any of them. If the number is divisible by any of these factors, it returns False, indicating that the input number is not prime. However, if the number is not divisible by any of these factors, it returns True, indicating that the input number is indeed prime. This process efficiently rules out divisors up to the square root of the number, significantly reducing the number of iterations required to make the determination. 

Here is a test suite that can be used to validate the function:
```python
# Test Suite
def test_is_prime():
    assert is_prime(101) == True
    assert is_prime(11) == True
    assert is_prime(13441) == True
    assert is_prime(61) == True
    assert is_prime(6) == False
    assert is_prime(4) == False
    assert is_prime(1) == False
```

To run the test suite, simply call the `test_is_prime()` function and assert the expected truthiness of each test case.