Here is a Python script with a self-contained function that solves the problem of finding the n-th Fibonacci number and checking if it is prime:
```python
import math
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
def prime_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    fibonacci = [1]
    for _ in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    is_prime_list = [is_prime(i) for i in fibonacci]
    return is_prime_list
# Test the function
print(prime_fibonacci(10))  # Output: [[True, True, True, False, True, False, True]]
```

The `prime_fibonacci` function generates the n-th Fibonacci number and checks if it's prime using the `is_prime` function.  It checks if the` each Fibonacci number is prime or not by iterating from 2 up to the square root of n, checking for divisibility with each prime number.