```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```
This function determines whether a given number is prime or not, and it passes all of the tests provided. The function is self-contained, meaning that it doesn't require any external inputs to function properly.

Let's break down the process of finding primality in this function:
1. Determine Base Conditions:
- If the number is less than or equal to 1, it is not prime.
- If the number is 2 or 3, it is prime.
2. Calculate Potential Critical Numbers:
- The number is 2 or 3, return True.
- If the number is not 2 or 3, use a loop to calculate the square root of the number, and check if the number is divisible by any integer whose square is less than or equal to the square root of the number.
3. Check Divisibility by Small Squares:
- The number is divisible by a square, return False.
- If the number is not divisible by any square, return True.

This is a straightforward and efficient method for determining whether a given number is prime. You can apply this with confidence to any given number to check its priminity.