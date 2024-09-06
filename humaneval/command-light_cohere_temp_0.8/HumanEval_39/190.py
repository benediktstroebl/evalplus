```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        a = 2
        b = 3
        while a < n:
            if is_prime(a):
                b = a
            a += 1
        return b

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
```
This function, `prime_fib` calculates the n-th Fibonacci number that is prime and returns it. 

It uses a basic iterative approach with some conditions to check if the number is prime or not. 

The function `is_prime` is a helper function to check if a number is prime or not. It uses the condition of `divisibility rules` to check if the number is divisible by any number from 2 up to the square root of the number.