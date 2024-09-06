Here's a solution that passes all the tests you provided:
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
This function checks if a number is prime by iteratively checking divisibility up to the square root of the number. It also checks for other divisibility of numbers equal to 2 and 3.

Please note that the code is self-contained and can be used as a stand-alone solution to determine if a given number is prime or not.