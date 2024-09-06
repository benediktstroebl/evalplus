```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It serves the purpose of calculating and returning the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where each number (known as a Fibonacci number) is the sum of the two preceding ones, starting from 0 and 1. Here's how the function operates, step by step:
1. The base case is defined with the condition `if n < 2:`. When n is either 0 or 1, the function immediately returns n without any further calculations. This is a fundamental approach to handle the first two numbers of the sequence since the Fibonacci sequence starts with 0 and 1.
2. For values of n greater than or equal to 2, the function employs a recursive approach to calculate the Fibonacci number. It uses the definition of the Fibonacci sequence, which states that a Fibonacci number is equal to the sum of the two preceding numbers in the sequence.

This recursive formula is the core of the Fibonacci sequence, and it's used to calculate the Fibonacci numbers for larger values of n.

It's important to note that while this function provides the correct result for the n-th Fibonacci number, it may not be the most efficient for large values of n due to the redundant recursive calculations. There are other, more efficient algorithms specifically designed for computing Fibonacci numbers, such as iterative approaches or matrix exponentiation. However, this basic recursive function serves as a straightforward and conceptually clear solution for small to moderate values of n.