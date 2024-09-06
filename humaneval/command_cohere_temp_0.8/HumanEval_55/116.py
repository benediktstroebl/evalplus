```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function implements the recursive formula for Fibonacci numbers. It returns the `n`-th Fibonacci number by recursively calling itself to calculate the preceding two Fibonacci numbers and adding them together. The base case is when `n` is less than or equal to 1, where it directly returns `n` as the first two Fibonacci numbers are 0 and 1. 

Here is an example of the output of the function for `n = 10`:
```python
>> fib(10)
55
```
This demonstrates that the function correctly calculates the 10th Fibonacci number, which is 55.