```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input and returns the n-th Fibonacci number. The base cases are handled efficiently, as the function returns n (or n-1) if n is 0 or 1, respectively. If n is greater than 1, the function recursively computes the n-th Fibonacci number by adding the (n-1)-th and (n-2)-th Fibonacci numbers, which is the essence of the Fibonacci sequence. This ensures the function accurately calculates the Fibonacci numbers for any given input.