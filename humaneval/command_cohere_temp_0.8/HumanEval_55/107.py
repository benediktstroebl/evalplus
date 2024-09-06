```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single argument n, which returns the nth Fibonacci number. The base case checks if n is less than or equal to 1, in which case it returns n, as the first two Fibonacci numbers are 0 and 1. If n is greater than 1, the function recursively calls itself with the arguments n-1 and n-2, and returns the sum of the results of these recursive calls, which will be the (n+1)th Fibonacci number. 

Here is an example usage of the function:
```python
>>> fib(1)
1
>>> fib(8)
21
>>> fib(10)
55
```
This output shows the function working correctly for the 1st, 8th, and 10th Fibonacci numbers, consistent with the problem statement. 
This approach, while simple, is not efficient, as each Fibonacci number is recursively calculated twice, leading to an exponential time complexity of O(2^n). However, it demonstrates the concept and gives a starting point for more advanced learners to then explore efficient algorithmic approaches. GLS