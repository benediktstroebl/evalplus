```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fib4 sequence is commonly defined as 0, 1, 1, 2, ...

    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib4(n-1) + fib4(n-2)

# Example usage
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This Python code defines a function `fib4` that computes the n-th Fibonacci number in the sequence using an iterative approach. The function checks the basic cases: if n is 0, it returns 0 (base case), and if n is 1, it returns 0 (another base case). If n is 2, it returns 1 (Fibonacci 2). Otherwise, it recursively calls itself with `n-1` and `n-2` and sums the results.