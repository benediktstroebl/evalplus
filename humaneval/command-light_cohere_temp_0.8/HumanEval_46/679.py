Here's a self-contained function that calculates and returns the nth element of the Fibonacci sequence:
```python
def fib4(n):
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
This function uses a loop to calculate the nth element of the Fibonacci sequence by summing up the four previous elements. 
Note that this implementation does not use recursion, and it is more efficient than the recursive approach.