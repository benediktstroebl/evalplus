```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function returns the n-th Fibonacci number. It starts with the base cases of `fib(0) = 0` and `fib(1) = 1`, and then recursively computes the subsequent Fibonacci numbers by adding the two previous numbers in the sequence. 
This approach leverages the inherent nature of the Fibonacci sequence, where each number is the sum of the two preceding ones, thus eliminating the need for explicit intermediate storage.