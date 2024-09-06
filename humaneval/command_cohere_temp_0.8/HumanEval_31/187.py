Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
This function defines a logical process for determining whether a given number n is prime. It begins by checking if n is less than 2, returning False if so, since primality requires numbers to be greater than 1. The function then initiates a loop from 2 up to the square root of n, checking whether n is divisible by any integer within this range. If there is a divisor, the function returns False, indicating that the number is not prime. However, if no divisor is found after exhausting the search range, the function returns True, indicating that n is indeed a prime number. 

Here is an example of an invocation of this function:
```python
print(is_prime(13441))
```
This will print:
```
True
```
This shows that the function considers 13441 to be a prime number.