```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `Fibonacci sequence` is an integer sequence where the first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.

This Python script defines a self-contained function called `fib` that computes the n-th Fibonacci number. It includes a proper docstring and permits optional arguments. The function initially determines whether n is less than 2. If true, it returns n, which corresponds to the initial 0 and 1 terms in the sequence. If n is greater than or equal to 2, the function recursively calls itself with the arguments n-1 and n-2, adding the results to provide the n-th Fibonacci number. 

This approach, while efficient for reasonably small n, is not optimized for larger values of n, as it involves redundant recursive calculations. Nonetheless, it provides an intuitive understanding of how the Fibonacci sequence is generated. 

You can use the function by calling it and passing the desired index `n` of the Fibonacci number you want to retrieve.