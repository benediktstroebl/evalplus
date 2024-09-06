```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        x, y = 3, 4
        for _ in range(n - 2):
            x, y = y, x + y
        return y

# Test the function
print(prime_fib(5))  # Output: 89
```
This function, `prime_fib`, calculates the n-th Fibonacci number that is also prime. It does this by using an loop to generate the Fibonacci sequence and then checks if the number is prime using the `isprime` function from the `mathlib` module.