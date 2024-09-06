```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The code defines a recursive function `fib` that calculates the n-th Fibonacci number by recursively calling itself with values `n-1` and `n-2` and returning their sum, or returning `n` if `n` is less than or equal to 1.  This follows the definition of the Fibonacci sequence, where each number is the sum of the two preceding ones, with the initial terms defined as `0` and `1`.  This logic is encapsulated in a function aimed at computing the n-th Fibonacci number, where the function arguments denote the desired index `n` in the sequence, and the returned value is the corresponding number in the sequence.  This is facilitated by the inherent nature of Python's definition and usage of functions.

Here is an example usage of the function:
```python
print(fib(10))
```

The output of this code will be:
```
55
```