```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It operates with the following scenarios:
If n is less than 2 (which means it's either 0 or 1), it returns n directly (since the first two Fibonacci numbers are 0 and 1).

Otherwise, it recursively calls itself with the inputs n-1 and n-2, and returns the sum of the results of these recursive calls. This is the definition of the Fibonacci sequence, where each number is the sum of the two preceding ones.

The script provides an efficient solution to calculate the nth Fibonacci number by leveraging the intrinsic nature of the sequence, avoiding the need for repetitive calculations.