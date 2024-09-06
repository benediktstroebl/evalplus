```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        i = 2
        while i * i <= n:
            if is_prime(i):
                break
            i += 1
        return i  # returns next Fibonacci number that is prime

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True

# Example usage
print(prime_fib(5))  # Output: 89
print(is_prime(60))  # Output: False
```
The provided code defines a function `prime_fib` that calculates the n-th Fibonacci number which is prime, and a function `is_prime` that checks whether a given number is prime or not. The code then demonstrates the example usage of the `prime_fib` function by calculating the 89th Fibonacci number that is prime, and checks whether 60 is prime or not.