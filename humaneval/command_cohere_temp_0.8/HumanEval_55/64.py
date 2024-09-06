```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It handles the base cases first, returning n (or 1, for n = 1) when n is less than 2. This ensures that the function correctly returns the first two Fibonacci numbers (0 and 1). For n greater than or equal to 2, it recursively calls itself with the arguments n-1 and n-2, and then adds the results, effectively calculating the Fibonacci number for the given input. This approach leverages the mathematical properties of the Fibonacci sequence, where each number is the sum of the two preceding ones, which makes the recursive definition intuitive and aligned with the sequence's pattern.