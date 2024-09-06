Here's a Python script with a self-contained function `is_prime` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function iterates through integers from 2 up to the square root of the input number `n`, checking for divisibility. If the number is divisible by any integer in that range, it returns `False`, indicating that the number is not prime. However, if the number is not divisible by any integer in that range, it returns `True`, indicating that the number is prime. This approach leverages the efficiency of an iterative strategy to determine primality. 

Here's an example of using the function:
```python
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

This demonstrates how the function can be used to determine whether different input numbers are prime or not.