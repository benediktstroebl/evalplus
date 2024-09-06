```python
def is_prime(n):
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
The function checks for primality by following these steps:
- If the number is less than or equal to 1, it is not prime.
- If the number is 2 or 3, it is prime.
- The function checks for divisibility by 2 and 3, returning False if the number is divisible by either.
- It then iterates from 5 up, checking for divisibility by the square of the current number, and its odd increments by 6.

This function can be used to efficiently determine whether a given number is prime or not, which is valuable in many cryptographic and algorithmic applications.