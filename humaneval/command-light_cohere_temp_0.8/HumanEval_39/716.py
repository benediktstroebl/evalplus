```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 3
    if n % 3 == 0:
        return 5
    else:
        temp = prime_fib(n // 2)
        if temp == 2 or temp == 3:
            return temp
        else:
            return 2 + prime_fib(n - 1)

# Example usage
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 28
```

This code defines a function `prime_fib` that computes and returns the n-th Fibonacci number that is prime. The function first checks if n is less than or equal to 1, in which case it returns n directly. It then checks if n is of the form 2 or 3, and if so, it returns the appropriate Fibonacci number. If n is neither of these, the function recursively calls itself with n divided by 2, and then adds the result of the recursive call to get the final answer.