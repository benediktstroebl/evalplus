```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer argument n. It returns the n-th Fibonacci number. The base case checks if n is less than 2, returning n if so. If n is greater than or equal to 2, it recursively calls fib with arguments n-1 and n-2 and adds the results, thereby calculating the n-th Fibonacci number. This code defines the function and allows it to be called with different values for n to produce the corresponding Fibonacci number.