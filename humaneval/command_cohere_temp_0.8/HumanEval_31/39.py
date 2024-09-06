Here's a Python script with a self-contained function `is_prime` that follows the problem statement and hopefully passes the tests provided:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```
This function iterates through integers from 2 up to the square root of the input number `n`, checking for divisibility. If the number is divisible by any integer in that range, it's not prime, and the function returns `False`. If not, it's prime, and the function returns `True`. 

The provided tests should be commented out as they are not self-contained (they rely on the `is_prime` function that this script is providing). Here's the commented out test suite:
```python
# Test the function:
def test_is_prime():
    # Basic cases
    assert is_prime(6) == False, "6 is not prime"
    assert is_prime(101) == True, "101 is prime"
    assert is_prime(11) == True, "11 is prime"
    assert is_prime(13441) == True, "13441 is prime"
    assert is_prime(61) == True, "61 is prime"
    assert is_prime(4) == False, "4 is not prime"
    assert is_prime(1) == False, "1 is not prime"
```