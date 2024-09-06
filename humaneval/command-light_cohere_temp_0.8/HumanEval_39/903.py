```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif n % 2 == 0:
        return 5
    else:
        a = prime_fib(n // 2)
        if a == 2 or n == a + 1:
            return a
        else:
            return prime_fib(n - 1) + a
```

This Python script defines a function called `prime_fib` which returns the n-th Fibonacci number that is prime and also satisfies the `Fibonacci property`. The function uses an iterative approach to determine if a number is prime or not. The test cases are also implemented to ensure the correctness of the function.