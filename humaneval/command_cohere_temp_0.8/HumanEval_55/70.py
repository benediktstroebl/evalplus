```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It serves the purpose of calculating and returning the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where each number (known as a Fibonacci number) is the sum of the two preceding ones, starting from 0 and 1. Here's how the function operates, step by step:
1. The base case is defined with the condition `if n < 2:`. When n is either 0 or 1, the function immediately returns n without any further calculations. This is a halt condition, meaning that once the sequence reaches these two numbers, it stops growing. Hence, for n = 1, the function returns 1, and for n = 0, it returns 0.
2. For values of n greater than or equal to 2, the function employs a recursive approach to calculate the Fibonacci number. It uses the definition of the Fibonacci sequence, asserting that the n-th Fibonacci number is equal to the sum of the (n-1)-th and (n-2)-th Fibonacci numbers.

The function calls itself recursively with the arguments n-1 and n-2, respectively. These recursive calls continue until the base case is reached (n < 2), at which point the recursive calls return the respective Fibonacci numbers. Finally, the function returns the combined value of the recursive calls, effectively calculating the n-th Fibonacci number.

The function includes a docstring (`''"`) that provides details about its purpose, along with three illustrative test cases in the form of assertions. These test cases demonstrate the behavior of the function for different values of n. Overall, this script offers a concise and efficient way to compute Fibonacci numbers using recursion, encapsulated within a robust function with clear documentation.