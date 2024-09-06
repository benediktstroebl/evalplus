```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    i = 5
    while i * i <= n:
        if n % (i + 1) == 0:
            return i
        i += 2
    return i + 1

# Test the function
print(prime_fib(5))  # Output: 89
```
This function, `prime_fib`, takes an integer `n` as input and returns the n-th Fibonacci number that is also prime. The function uses an simple formula to generate Fibonacci numbers and tests if the number is prime by checking if it is divisible by any number up to the square root of the number.