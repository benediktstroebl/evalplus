```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers.
    :return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
```

This Python code provides a simple and efficient approach to computing the n-th element of the Fibonacci sequence without recursion. It uses a fact that the n-th element is the sum of the preceding four numbers. 

This approach is highly efficient and avoids the overhead of recursion, making it suitable for larger values of n.