```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `Fibonacci sequence` is an integer sequence where the first two terms are 0 and 1. All other terms are obtained by adding the preceding two values. Although there is no closed form for the nth Fibonacci number, recursive approaches like the one used in this script offer an effective solution. This function returns the nth Fibonacci number based on the definition of the sequence. It starts with 0 and 1, then continues by adding the two previous numbers to arrive at the next number in the sequence.