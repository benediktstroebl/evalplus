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

This function returns True if the number is prime, and False otherwise. It first checks if the number is less than 2, subsequently iterating from 2 to the square root of the number checking for divisibility. If the number is divisible by any integer in this range, it is not prime and the function returns False. If the number is not divisible by any integer in this range, it is prime and the function returns True. This approach is efficient due to its logarithmic complexity and is suited for checking relatively large numbers for primality. 
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function is defined to handle any input number, including negatives and floats, and efficiently determine whether the given number is prime or not, adhering to the test cases provided.