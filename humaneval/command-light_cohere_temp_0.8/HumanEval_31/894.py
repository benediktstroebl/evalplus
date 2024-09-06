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

This function, `is_prime()`, determines whether a given number is a prime or not. It begins by checking for numbers less than or equal to 1 and 3, which are obviously prime. Then, it checks for numbers that are divisible by 2 or 3, returning False if they are.

Next, the function determines whether the given number is divisible by any number from 5 to the square root of the number minus 1. It then iterates through these process by incrementing 6 until the square root of the number exceeds it.

Finally, if the number passes all these tests, it is considered prime and the function returns True, otherwise, it returns False. 

This function can be used to check whether a given number is prime or not, and it passes all the corresponding tests.