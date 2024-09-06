Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function is designed to determine whether a given number is prime. It begins by checking if the number is less than 2, returning False if so, as numbers less than 2 are not prime. The function then iterates through numbers from 2 up to the square root of the input number, checking for divisibility. If the number is divisible by any integer within this range, it's not prime, and the function returns False. However, if the number isn't divisible by any integer within this range, it's prime, and the function returns True.

This algorithm, while straightforward, is efficient for prime checking since it involves checking only up to the square root of the number, eliminating the need to check larger numbers that would just be divisors of the smaller ones.

To provide further insight, the code snippet below is a test suite with example tests that cover different cases:
```python
# Test Suite
def test_is_prime():
    assert is_prime(101) == True, "Expected 101 to be prime"
    assert is_prime(11) == True, "Expected 11 to be prime"
    assert is_prime(13441) == True, "Expected 13441 to be prime"
    assert is_prime(61) == True, "Expected 61 to be prime"

    assert is_prime(6) == False, "Expected 6 not to be prime"
    assert is_prime(4) == False, "Expected 4 not to be prime"
    assert is_prime(1) == False, "Expected 1 not to be prime"

test_is_prime()
```

This test suite covers multiple scenarios, validating the behavior of the `is_prime` function for both prime and non-prime numbers.

In summary, the `is_prime` function efficiently identifies prime numbers by checking divisibility only up to the square root of the number, and the test suite ensures its accuracy across various input scenarios.