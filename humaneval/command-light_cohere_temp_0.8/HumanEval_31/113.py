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
The above Python function, 'is_prime', checks whether a given number 'n' is a prime number. The function first checks if 'n' is less than or equal to 1, returning 'False' if it is, as prime numbers must be greater than 2. Then, it checks if 'n' is of the small prime numbers, returning 'True' if it is and proceeding to the next test. 

The function then uses the 'if-else' statement to check for divisibility by 2 or 3, returning 'False' if 'n' is divisible by either of these numbers. Then, it starts a loop from 5 upwards, checking if 'n' is divisible by the square of the loop variable 'i' or the sum of 'i' and '2'. The loop will continue until the square of 'i' exceeds 'n', and the function will return 'True' if 'n' is not divisible by any perfect square.