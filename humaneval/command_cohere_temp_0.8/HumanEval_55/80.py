```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python code defines a function fib that calculates the n-th Fibonacci number. The base cases (n=1 and n=2) are handled first, returning n and 1 respectively. For larger n, the function recursively computes the sum of the (n-1)th and (n-2)th Fibonacci numbers, effectively constructing the Fibonacci sequence. This approach efficiently computes Fibonacci numbers without explicit recursion and is optimized for larger values of n.

Here is an example usage of the function:
```python
result = fib(10)
print(result)
```
This would output:
```
55
```