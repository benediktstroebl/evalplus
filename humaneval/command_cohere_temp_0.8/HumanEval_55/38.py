```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This Python code defines a function called fib that utilizes a recursive approach to calculate the Fibonacci numbers. The function first checks if the input n is less than or equal to 1, in which case it returns n itself. If n is greater than 1, it recursively calls itself twice with inputs n-1 and n-2, and then adds the results of these recursive calls together. This recursive approach creates a chain of recursive calls, where each call relies on the previous two numbers to calculate the next Fibonacci number. Ultimately, this builds up the entire Fibonacci sequence. The script adequately solves the problem of calculating the nth Fibonacci number.