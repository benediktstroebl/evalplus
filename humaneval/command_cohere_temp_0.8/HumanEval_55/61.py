```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It serves the purpose of calculating and returning the n-th Fibonacci number. The Fibonacci sequence is a series of numbers in which each number (known as a Fibonacci number) is the sum of the two preceding ones, starting from 0 and 1. Here's how the function operates, step by step:
1. The base case is defined with the condition `if n < 2:`. When n is either 0 or 1, the function instantly returns n without any further calculations. This is a practical approach for these initial values because the Fibonacci sequence starts with 0 and 1, ensuring that the function returns the correct values for these two straightforward cases.
2. For values of n greater than or equal to 2, the function employs a recursive approach to calculate the Fibonacci number. It uses the recursive equation of the Fibonacci sequence, which is that the n-th Fibonacci number is equal to the sum of the (n-1)-th and (n-2)-th Fibonacci numbers.

The function recursively calls itself twice, with arguments n-1 and n-2, respectively. The recursive calls continue until the base case is reached (n < 2), at which point the recursive calls start returning the values back up the chain, and the function accumulates the values to obtain the final Fibonacci number for the given n.

The function includes a docstring (`''"`) that provides details about its purpose, as well as example outputs (`'`') for the function's behavior when provided with different values of n. These example outputs are structured as test cases and demonstrate the function's expected behavior.

By employing this function, you can efficiently calculate any Fibonacci number for a given value of n in Python, avoiding the need for explicit loops or iterative approaches that might lead to performance issues for larger values of n. The recursive solution's scalability may be limited by its nature, yet it elegantly captures the mathematical essence of the Fibonacci sequence.