```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The code defines a recursive function `fib` that calculates the n-th Fibonacci number by recursively calling itself with inputs n-1 and n-2, alternating until n equals 1, at which point it returns n. This follows the definition of Fibonacci numbers where each number is the sum of the two preceding ones, and the base cases are 0 and 1.