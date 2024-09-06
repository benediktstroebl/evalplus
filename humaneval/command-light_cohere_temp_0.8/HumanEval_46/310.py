```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    return:
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 2
        else:
            return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    ```

This code defines a function called fib4 that computes the n-th element of the Fibonacci sequence. The function uses a conditionals to determine the base cases (n=0, n=1, n=2) and then recursively computes the Fibonacci number for n by summing the previous four Fibonacci numbers. 

This self-contained solution eliminates the need for external recursion and maintains a clear and concise structure.