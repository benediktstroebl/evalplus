```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function uses recursion to calculate the nth Fibonacci number. It checks if `n` is less than or equal to 1, returning `n` if true. If `n` is greater than 1, it returns the sum of the (`n-1`)th and (`n-2`)th Fibonacci numbers. This algorithm's base cases ensure that it correctly returns the first two Fibonacci numbers (1 and 1) for `n` equal to 1 and 2, respectively. As `n` increases, the algorithm leverages the intrinsic nature of Fibonacci numbers, where each number is the sum of the two preceding ones, enabling efficient computation. 

Here is an example usage of the function provided:
```python
result = fib(10)
print(result)
```

And here is the output of this usage:
```
55
```