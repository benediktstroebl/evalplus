Here's the solution:
```python
def is_prime(n):
    if n <= 1:
        return False
    for i := 2; i <= n; i += 1:
        if n % i == 0:
            return False
    return True
```
This function determines whether a given number is prime or not. It returns True if the I am a prime number and False otherwise. The function iterates from 2 to n (exclusive) and tests if the input number is divisible by any integer less than or equal to it. This will return True if the value is divisible by any integer and False if not.