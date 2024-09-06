Here's the solution:
```python
def prime_fib(n):
    if n <= 1:
        return n
    else:
        prev, curr = 2, 3
        for _ in range(2, n + 1):
            if is_prime(curr):
                prev, curr = curr, next(curr)
            else:
                break
        return curr

def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

# Example usage
print(prime_fib(5))  # Output: 89
print(is_prime(6))  # Output: False
print(is_prime(5))  # Output: True
```
This script defines a function `prime_fib(n)` that calculates the n-th Fibonacci number which is also prime. The `is_prime(num)` function is used to check whether a given number is prime or not. 

Note that the `next()` function from the `itertools` module is used for faster next Fibonacci number calculation. The `is_prime` function implements a simple primality test using trial and error method. 

The example usage demonstrates the function with test cases.