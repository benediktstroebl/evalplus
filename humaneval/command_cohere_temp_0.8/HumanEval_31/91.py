Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
This function defines a logic pipeline that handles edge cases and conforms to the provided test cases. It first checks if the number is less than 2, which would make it false, then it checks if the number is divisible by any number from 2 to the square root of the number, if it is, it returns false, if it isn't, it returns true. 
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
This will return True for prime numbers and False for non-prime numbers based on the provided test cases.