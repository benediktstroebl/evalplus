```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `Fibonacci Sequence` often referred to as Fibonacci numbers, is an integer sequence where the first two terms are 0 and 1. All other terms are obtained by adding the preceding two values. This sequence is named after Leonardo of Pisa, who was known as Fibonacci.

The Python script provides a self-contained function `fib` that calculates the nth Fibonacci number. It employs a recursive approach to solve this problem. The function checks if `n` is less than or equal to 1. If so, it returns `n` directly, as the first two numbers in the Fibonacci sequence are 0 and 1. If `n` is greater than 1, the function recursively calls itself, adding the results of the previous two calls to calculate the Fibonacci number for `n`. This recursive approach mirrors the recursive definition of the Fibonacci sequence. 

The function includes a docstring that showcases the expected behavior of the function through examples. These examples are extracted in a mechanically parseable format, like CSV, when the docstring is formatted with the standard Python format. This development approach promotes more comprehensive and readable functions and increases the function's accessibility to newcomers.