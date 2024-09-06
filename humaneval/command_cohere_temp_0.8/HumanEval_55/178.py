```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This Python script defines a self-contained function called fib that takes an integer n as input and returns the n-th Fibonacci number. The script first handles the base cases of n=1 (where the function returns 1) and n=0 (where the function returns 0) by using the if statement to determine if n is less than or equal to 1. If n is greater than 1, the function recursively calls itself to calculate the sum of the previous two Fibonacci numbers, effectively building the Fibonacci sequence. 

This approach leverages the intrinsic nature of Fibonacci numbers, where each number is the sum of the two preceding ones, ultimately leading to efficient computation. The function's initial call to fib(n) kicks off this recursive process, and successive calls continue to build the sequence until the base case is met, at which point the accumulated value is returned as the n-th Fibonacci number. 

The function utilizes a recursive approach, which is an elegant solution for calculating Fibonacci numbers due to their inherent structural relationship. However, it's worth noting that due to the repetitive nature of this computation, this particular approach could lead to performance issues for larger values of n. If efficiency is a concern, alternative approaches could be considered, such as memoization or an iterative approach. Nonetheless, this solution elegantly demonstrates the fundamental concept of recursion in solving the Fibonacci sequence. 

To address the edge cases handled in the requested solution, a final check for n <= 1 is included to ensure fib(n) returns the correct value for the first two Fibonacci numbers. When the function is called with n = 10, it recursively computes fib(9) + fib(8), then fib(7) + fib(6), and so on, until reaching fib(1) + fib(0), resulting in 55 as the final output. This reflection demonstrates the complete working of the fib function, from handling the initial call to managing the recursive flow and returning the appropriate values. 

Additionally, here's a Markdown code block with proper formatting and syntax highlighting that demonstrates the Python script:
```
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
```
This code block provides a clear and readable version of the solution, making it easier for users to view and understand the code. Let me know if I can assist in explaining any part of the provided code or offering further suggestions!