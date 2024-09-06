```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This Python code defines a function fib that calculates the n-th Fibonacci number. The base case checks if n is less than or equal to 1, returning n if so. Otherwise, the function recursively computes the sum of the (n-1)-th and (n-2)-th Fibonacci numbers, utilizing the Fibonacci sequence's intrinsic nature of each number being the sum of the two preceding ones. 

Here is an example usage of the function for the 3rd Fibonacci number:
```python
answer = fib(3)
print(answer)
```
This would print out `2` as the 3rd Fibonacci number is `2`. 

This approach, while elegant in its simplicity, is inefficient for large n due to the redundant recursive calculations. Optimized approaches like memoization or bottom-up dynamic programming offer more efficient solutions. Nonetheless, this code serves as a fundamental introduction to recursion and problem-solving in Python.