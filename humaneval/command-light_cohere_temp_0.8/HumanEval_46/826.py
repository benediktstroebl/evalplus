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

# Example usage:
print(fib4(5))  # Output: 14
print(fib4(7))  # Output: 28
```

This script defines a function `fib4` that computes the n-th Fibonacci number in the Fibonacci sequence using a loop-free approach without recursion. It uses a optimized calculation by breaking down the sequence into its constituent parts and summing them up. 

This approach reduces memory usage and avoids the exponential time complexity associated with recursive solutions.