```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This Python script defines a self-contained function called fib that takes an integer n as input and returns the n-th Fibonacci number. The base cases are handled efficiently, as the function immediately returns n or 1 for n equal to 0 or 1, respectively. For larger values of n, it recursively computes the Fibonacci number by summing the two previous numbers in the sequence, demonstrating the classic definition of the Fibonacci sequence.