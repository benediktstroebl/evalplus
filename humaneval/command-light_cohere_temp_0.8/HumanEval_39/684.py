Here is a Python script that defines a function called `prime_fibonacci` which returns the n-th Fibonacci number that is also prime:

```python
def prime_fib(n: int):
    """
    prime_fib returns the n-th Fibonacci number that is prime.
    The function first returns the value of 2, and then checks subsequent numbers to verify if they are prime.
    """
    first check is the previous numbers, if they are not prime, it will return the next number.
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        for i in range(4, n+1, 2):
            if is_prime(i):
                return i
    return None

def is_prime(n: int):
    """
    checks if n is prime or not
    """
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

# Example usage
print(prime_fib(5))
```

This script defines a function called `prime_fib` which returns the n-th Fibonacci number that is prime. The function first returns the value of 2 and then checks subsequent numbers to verify if they are prime, by checking if the number doesn't have divisors less than or equal to its square root, if the number does, it will return the next number.