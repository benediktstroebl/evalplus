Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function returns true if the given number is prime, and false otherwise. It checks if the given number is less than 2, and if so, it returns false. It then iterates from 2 up to the square root of the given number, checking whether the given number is divisible by any of these numbers. If it is, it returns false. If it isn't, it returns true.

Here is an example of how to use the function:
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

As you can see, the function returns the expected results based on the given test cases.