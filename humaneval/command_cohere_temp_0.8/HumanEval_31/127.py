Here's a Python script with a self-contained function that solves the prime determination problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function is crafted to efficiently determine whether a given number n is prime. It starts by handling the special case of n being less than 2, ensuring that the function returns False since prime numbers always exceed 1. The function then initiates a loop from 2 up to the square root of n. This loop examines whether n is divisible by any integer within this range. If any such divisor is found, the function promptly returns False, indicating that the number is not prime due to having a divisor other than 1 and itself. However, if no divisor is encountered, the function returns True, signifying that the number is prime. This approach ensures both accuracy and efficiency in prime determination.