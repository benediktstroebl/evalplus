Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function defines a logical flow to determine whether a given number is prime. It first handles the edge case of numbers less than 2, then checks for divisibility from 2 up to the square root of the number, and finally, if no divisors are found, it confirms the number as prime. 

This approach results in an efficient algorithm with a time complexity of O(sqrt(n)), which is a standard practice for checking primality in scenarios where computational efficiency is necessary.