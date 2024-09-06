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
This function, named as **`is_prime`**, efficiently determines whether a given number is a prime, using basic prime number criteria and an optimized loop that checks divisibility up to the square root of the number.

The function begins by excluding obviously non-prime numbers and numbers equal to 2 and 3. It then employs a optimized technique to efficiently test for primality up to the square root of the input number.  The loop checks for divisibility by attempting squares and adjacent even numbers, which are the most efficient for this purpose.  The function then correctly identifies prime numbers and returns True if the input number is prime, and False otherwise.