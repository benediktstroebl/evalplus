```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python code defines a function called fib that fulfills the role of computing the nth Fibonacci number. The function employs a recursive approach, leveraging the fact that the Fibonacci sequence is defined by the recurrence relation: Fib(n) = Fib(n-1) + Fib(n-2). For instances where n is either 1 or 2, the function provides an appropriate direct return value. As the program's primary intent is to illustrate how to compute Fibonacci numbers, it does not employ sophisticated algorithms to tackle the sequence's intrinsic exponential growth; instead, it relies on the inherent nature of the sequence. Consequently, this function efficiently calculates the Fibonacci sequence, making it useful for a variety of mathematical and algorithmic applications.