Here's the code:
```python
def is_prime(n):
    """
    Check if a number is prime or not. 
    """
    returns True if n is a prime number and False otherwise.
    
    if n <= 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 6
    return True
```
The function checks if the given number is prime or not. It uses the series of checks:
- If the number is less than or equal to 1, then it's definitely not a prime number.
- If the number is divisible by 2 or 3, it returns True immediately.
- Otherwise, the number must be divisible by neither 2 nor 3 but a perfect square of 5, so the loop starts from 5 and adds 6 to the loop variable until it reaches the square root of the number.

It uses the condition that the square root of a prime number should be odd to ensure that the number is prime.