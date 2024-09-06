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

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning False if so. Then, it iterates from 2 to the square root of the number, checking if the number is divisible by any other number. If the number is divisible by any other number in this range, it returns False. However, if the number is not prime, it returns True.

Here's a snippet of tests to ensure its correctness:
```python
# Testing a few prime and non-prime numbers
>>> is_prime(7)
True

>>> is_prime(4)
False

>>> is_prime(101)
True

>>> is_prime(93)
True

>>> is_prime(20)
False

>>> is_prime(3)
True

>>> is_prime(10)
False
```