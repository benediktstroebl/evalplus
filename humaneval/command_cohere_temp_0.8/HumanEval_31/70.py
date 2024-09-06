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

This function returns true if the given number is prime, and false otherwise. It runs through a series of tests to determine if the number is divisible by any other number, and if so, it is not prime. If the number is not divisible by any other number, it is considered prime. The function's concise structure enables efficient prime number identification, as confirmed by the provided test cases.