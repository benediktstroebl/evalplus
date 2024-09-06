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

This function adheres to the problem statement and satisfies the provided test cases. It checks if a number is less than 2, it returns False; if the number is equal to 1, it also returns False; and for all other numbers, it checks if the number is divisible by any number from 2 to the square root of the number, if so, it returns False; otherwise, it returns True.