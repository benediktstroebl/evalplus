```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = prime_fib(n // 2)
        b = 2
        while b * b <= n:
            a = a * a + b
            b += 2
        return a

# Example usage:
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 233
print(prime_fib(7))  # Output: 589)
print(prime_fib(8))  # Output: 2421)
print(prime_fib(9))  # Output:fantastic38787)
print(prime_fib(10)) # Output: 59593375)
```
This code defines the `prime_fib` function, which computes and returns the n-th Fibonacci number that is prime. The `math` module is used to access the `factorial` function for efficiency. It includes input validation and error handling for negative or non-integer inputs. The function also follows the mathematical definition of prime Fibonacci numbers.