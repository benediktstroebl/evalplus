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
This function, `is_prime`, returns True if the given number is prime and False otherwise. It uses trial and well known test for primality, checking divisibility by 2 and 3, then using a simple loop to further test divisibility up to the square root of the number.