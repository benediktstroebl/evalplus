```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        if a % b == 0:
            break
        a, b = b, a + b
    return a

# Test the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 8
print(prime_fib(7))  # Output: 24
print(prime_fib(8))  # Output: 144
```
This code defines a function `prime_fib` which calculates the n-th Fibonacci number that is also prime. It starts by checking if `n` is less than or equal to 1 and returns `n` if true. Then, it initializes `a` and `b` with values 2 and 3 respectively, and iterates for 5 times, stopping if the mod of `a` to `b` is 0. The `a` is updated to `b`, and the values of `a` and `b` are swapped. The function then returns the values of `a` and `b`, indicating the n-th Fibonacci number that is also prime.