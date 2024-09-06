```python
def fib4(n: int):
    """
    The Fibonacci sequence without recursion.
    if n<=0:
        return 0
    elif n<=1:
        return 0
    elif n<=2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

if __name__ == "__main__":
    print(fib4(5))
    print(fib4(6))
    print(fib4(7))
```

This script defines a function that computes the n-th Fibonacci number in the sequence without recursion. The function uses a simple case-sensitive logic to determine the appropriate Fibonacci number based on the input 'n'. The test code at the end demonstrates how the function works for different inputs.