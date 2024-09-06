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

This function should be self-contained and should work correctly for the test cases provided, including edge cases like `n = 1` and `n = 4`. 

To implement this, it first checks if the given number is less than 2, returning False in such cases. It then iterates from 2 to the square root of the number, checking for divisibility. If the number is divisible by any integer in this range, it returns False. If it isn't, it returns True, indicating that the number is prime.  This should hopefully address the test cases provided. 
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```