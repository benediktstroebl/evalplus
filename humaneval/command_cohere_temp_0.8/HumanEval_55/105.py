```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single argument n, which returns the nth Fibonacci number. The base case checks if n is less than or equal to 1, in which case it returns n, as the first two Fibonacci numbers are 0 and 1. If n is greater than 1, the function recursively calls itself, with arguments n-1 and n-2, and adds the results to produce the nth Fibonacci number. This code defines a single function that can return the nth Fibonacci number for any input n, and its behavior is summarized within the function itself.  This allows users to quickly understand the purpose and usage of the function without relying on external documentation. 
The help text is still included, as it provides information on the expected type of the argument (int) and provides example usage, which is useful for users to quickly understand the function's behavior and its expected input. In this updated version, the help text is properly formatted with two spaces of indentation, and the examples now use the `>>>` marker, which is the standard convention for indicating example usage in Python.

Here is the code with updated markdown:
```python
def fib(n: int):
    """
    Return n-th Fibonacci number.

    :param n: Number of the Fibonacci number to return
    :type n: int

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```