```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It serves the purpose of calculating and returning the n-th Fibonacci number. The Fibonacci sequence is a series of numbers in which each subsequent number is the sum of the two preceding ones, starting from 0 and 1. This sequence is commonly known as 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on. The function employs a recursive approach to solve the problem. It uses a base case to return n or 1 for n equal to or less than 1. This is consistent with the first two numbers of the Fibonacci sequence. When n is greater than 1, it recursively calls itself with arguments n-1 and n-2, and then adds the results of these recursive calls to obtain the n-th Fibonacci number. This approach leverages the mathematical definition of the Fibonacci sequence, avoiding the need for explicit looping constructs.