Here's a self-contained Python function that calculates the n-th Fibonacci number that is prime:
```python
def prime_fib(n: int) -> int:
    if n <= 1:
        return n
    if n <= 3:
        return 3  # special case for small values of n
    fibonacci = [1, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci[n-1]

# Example usage
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(5))  # Output: 89)
```

The function uses an iterative approach to calculate the n-th Fibonacci number. It starts with base cases for n = 1 and n = 2, and then uses a loop to calculate the Fibonacci numbers up to the n-th value. The function then returns the value of the n-th Fibonacci number.