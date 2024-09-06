Here is a self-contained Python function that determines whether a given number is a prime, and it passes all of the tests provided:
```python
def is_prime(n):
    """Returns true if n is prime, and false otherwise."""
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
This function accepts an integer n as input and outputs a boolean value that indicates whether n is a prime number or not. 

It uses a trial and error approach, initially testing small numbers and then more significant numbers up to the square root of the input. It also checks divisibility from 2 and 3, as well as any number that is divisible by both is not prime, since they can be factored out by 2 or 3, respectively. 

The function is straightforward and uses basic mathematical primality testing to determine whether a number is prime or not.