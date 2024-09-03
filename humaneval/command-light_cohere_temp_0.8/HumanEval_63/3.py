```python
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

# Test cases
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24

```
This code defines the `fibfib` function that calculates the nth element of the Fibonacci sequence using recursion. The base cases for n equal to 0, 1, and 2 are defined, which are followed by the recursive calls to `fibfibfib(n-1)` and `fibfibfib(n-2)`. The test cases cover the expected outputs for various values of `n`.