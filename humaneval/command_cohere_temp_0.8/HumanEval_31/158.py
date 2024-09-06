Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function defines a logical order of steps to solve the issue, which includes checking if the number is below 2, performing a loop from 2 to the square root of the number, and checking if the number is divisible by any number in this range. Finally, it returns True if the number is not divisible by any number in this range and finally returns False if the number is divisible by any number in this range. 

This Python script solves the problem in a self-contained manner, as it does not rely on any external variables or functions.  It can be used directly to test any given number to determine if it is prime. 

This function also passes the provided tests in the markdown code block, as it returns the expected output for each test case:
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