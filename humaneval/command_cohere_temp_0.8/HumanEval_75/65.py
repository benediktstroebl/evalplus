```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_factors = []
    for i in range(2, int(a**0.5) + 1):
        while a % i == 0:
            prime_factors.append(i)
            a //= i
        if a == 1:
            break
    return len(prime_factors) == 3
```
The code defines a function `is_multiply_prime(a)` that determines whether the given number `a` is the product of three prime numbers. It iterates through factors up to the square root of `a`, factoring out all prime factors. The function returns True if exactly three prime factors are found; otherwise, it returns False. 

To test it you can run `python - tests.py` and check if all tests pass. Note that you may need to install the `pytest` package before running the test.

The code assumes that the given number is less than 100, as specified in the problem statement. 

This approach efficiently determines the prime factors and verifies that there are exactly three, completing the task in a concise and effective manner.