Here is a self-contained Python script that solves the problem of finding the largest divisor of a given number n:
```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number divisible by n that is less than n"""
    return n // 2  # A simple solution using divisibility rules.
```

This script defines a function called largest_divisor that takes in an integer n as input and returns the largest number divisible by n that is less than n. 

The function uses the concept of divisibility, where numbers that are divisible by n are all numbers that are multiples of the divisors of n, which are all the numbers less than n that divide n evenly. 

This is a simple and efficient solution that uses the divisibility rules of numbers.