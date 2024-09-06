```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `Fibonacci sequence` is an integer sequence where the first two terms are 0 and 1. All other terms are obtained by adding the preceding two values. Although there is no closed form for the nth Fibonacci number, this sequence can be recursively calculated. This function implements that recursion. 

Here is an example of how to use this function:
```python
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
```
This demonstrates the `fib` function's correctness for the 1st, 8th, and 10th Fibonacci numbers.