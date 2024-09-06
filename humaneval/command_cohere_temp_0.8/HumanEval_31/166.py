Here's a Python script with a self-contained function `is_prime(n)` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the given number is less than 2, returning False if so. Then, it iterates from 2 up to the square root of the number, checking whether the number is divisible by any integer in that range. If the number is divisible by any of them, it returns False. However, if neither condition is met until the end of the iteration, it returns True, indicating that the number is prime. 

This implementation provides an efficient way to check for primality, and it is robust enough to handle a wide range of inputs. 

Here is how you can test this function against the provided tests to see if it behaves as expected: 

```python
# Test if the function behaves as expected with the provided tests
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```

The function should return the expected answers for each test, and accordingly, each test should return the expected result.