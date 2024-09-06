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
This function, `is_prime`, determines whether a given number n is prime or not. It employs several conditional checks to eliminate non-prime numbers and then uses a loop with a progressively larger value, `i`, to check for divisibility up to the square root of the number. The function successfully passes all tests and is self-contained, as it can be called with various input values and returns the correct results.