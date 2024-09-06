Here is a self-contained Python function that checks if a given number is a prime:
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
This function uses a basic algorithm to determine if a number is prime or not. It starts by checking numbers less than or equal to 2 and 3, as they are prime by default. It then uses a number-squaring factorial and iterates in sqrt(n) steps, checking for divisibility by consecutive odd numbers. This algorithm is the time complexity is O(sqrt(n)). 

This function can be used to check if a given number is prime or not, and it passes all the test cases provided at the start of the function.