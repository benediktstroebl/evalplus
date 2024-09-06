Here's a Python script with a self-contained function `is_prime` that follows the problem statement and passes the tests provided:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function iterates through integers from 2 up to the square root of the input number `n`, checking for divisibility. If the number is divisible by any integer in that range, it's not prime, and the function returns `False`. If not, it's prime, and the function returns `True`. This approach is efficient due to the optimization involved hunting for divisors only up to the square root of the number, not exceeding it. 

The provided tests would be something like:
```python
# Testing the is_prime function
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

This way, you can run the tests inside the Python interpreter directly, and they will serve as our validation suite.  This function should now efficiently determine whether an input number is prime or not. 

Do you need assistance with anything else? Feel free to ask, and I'll gladly help!