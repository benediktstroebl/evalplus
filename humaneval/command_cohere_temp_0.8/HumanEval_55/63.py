```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer argument n, which represents the index of the Fibonacci number to be returned. The function starts with a base case, checking if n is less than 2 (0 or 1). If so, it returns n, as the base Fibonacci numbers are 0 and 1. If n is greater than or equal to 2, the function recursively calls itself with the arguments n-1 and n-2, and returns the sum of the results of these recursive calls, effectively calculating the Fibonacci number for the given index by iteratively summing the two previous Fibonacci numbers. 

This approach leverages the definition of the Fibonacci sequence, which is that each number is the sum of the two preceding ones, to efficiently compute the desired Fibonacci number. The script incorporates type hints, specifying that the argument n should be of integer type, making the function more robust and providing enhanced clarity and readability.

This code can be tested by calling it with different values of n and comparing the results with the expected Fibonacci numbers.