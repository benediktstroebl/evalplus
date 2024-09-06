```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        return_value = 3
        for i in range(5, n + 1, 6):
            if is_prime(i):
                return_value = i
        return_value

def is_prime(n: int):
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

# Test the functions
print(prime_fib(5))
print(is_prime(5))
``` 
The code defines a function `prime_fib` that computes the n-th Fibonacci number that is prime and returns it. 

This function uses an optimized approach with a loop from 5 to n, testing divisibility by 2, 3, and the square of the current number, up to the square root of n. 
The `is_prime` function tests for primality by checking if a number is less than or equal to 1, and if it's less than or equal to 2 and 3, but greater than their respective squares. 
The function then iterates a square loop, testing divisibility by the square of each number up to the square root of the current number, before returning `True` if the number is not divisible by any of those numbers. 
The test function returns `True` if the number is prime, and `False` otherwise.