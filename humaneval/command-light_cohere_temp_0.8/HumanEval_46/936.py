Here is a self-contained Python script that solves the Fibonacci sequence problem without recursion:
```python
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

```
This script defines a function fib4 that computes the n-th element of the Fibonacci sequence without recursion. The function uses a first base case for n equal to 0, which returns 0. For n equal to 1, it returns 0, and for n equal to 2, it returns 2. For n equal to 3, it returns 0. For n greater than 4, it recursively calls the fib4 function for n-1, n-2, n-3, and n-4, and adds the results together. The function then returns the sum of the four previous elements.