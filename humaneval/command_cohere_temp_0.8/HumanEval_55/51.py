```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The code defines a Python function called `fib` that calculates the n-th Fibonacci number. The base case checks if n is less than or equal to 1, returning n if so. Otherwise, the function recursively computes the sum of the (n-1)th and (n-2)th Fibonacci numbers, utilizing the fact that each Fibonacci number can be derived from the sum of the two preceding ones. This script showcases the use of recursion to solve mathematical problems.

Here is an example of how to use this function:
```python
result = fib(8)
print(result)  # Output: 21
```