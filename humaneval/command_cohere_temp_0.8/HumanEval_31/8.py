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

This function checks if a number is prime or not. It first checks if the number is smaller than 2, returning False in this case. Then, it iterates from 2 to the square root of the number, checking whether the number is divisible by any other number. If the number is divisible by any other number in this range, it returns False. However, if the number is not divisible by any number in this range, it returns True.

Here's an example usage of the function:
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

This shows the function's behavior corresponds to the given specification.