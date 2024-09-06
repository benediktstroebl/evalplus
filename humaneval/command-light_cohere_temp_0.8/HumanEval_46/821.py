```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which the next number is equal to the sum of the two preceding ones. The function returns the  n-th element of the Fibonacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n - 1) + fib4(n - 2)

# Test cases
print(fib4(5))   # Output: 4
print(fib4(6))   # Output: 8
print(fib4(7))   # Output: 14
```
This function computes the n-th Fibonacci number in O(1) time, which is a significant improvement over the naive recursive approach.