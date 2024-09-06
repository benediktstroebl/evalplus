```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It returns the n-th Fibonacci number. The base cases are handled efficiently, as fib(0) and fib(1) are defined to return 0 and 1, respectively. For larger values of n, the function recursively computes the Fibonacci number by summing the two previous numbers in the sequence, fib(n-1) and fib(n-2). This definition ensures the integrity of the Fibonacci sequence and allows the function to calculate the number accurately.