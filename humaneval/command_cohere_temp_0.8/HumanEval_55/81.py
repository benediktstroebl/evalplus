```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This function uses a recursive approach to calculate the Fibonacci sequence, which is an efficient way to solve this type of problem. It provides an elegant solution that fits in a single function, making it both self-contained and easy to maintain. 
To test this function, you can call it with different input values and compare the results against the Fibonacci sequence to ensure it produces the correct nth number.  For example:
```python
# Test the function
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(10) == 55
``` 
This demonstrates that the function correctly calculates the Fibonacci sequence to confirm its behavior matches the problem statement.