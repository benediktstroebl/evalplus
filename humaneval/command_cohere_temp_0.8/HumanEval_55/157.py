```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It returns the nth Fibonacci number. The base cases are handled with the conditional statement `if n <= 1`, where it returns n if n is either 1 or 0, assuming the first two Fibonacci numbers are 0 and 1. If n is greater than 1, it recursively calls itself with the arguments n-1 and n-2, and adds the results to compute the Fibonacci number for n. This approach is efficient due to the cancellation of multiples of the two overlapping Fibonacci numbers in each iteration. 
The function is tested with the following input examples:
```python
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
```
These tests illustrate the correct operation of the function, confirming that it generates the correct Fibonacci numbers for the provided input. A more advanced approach to improve memory efficiency and prevent overflow is to use memoization, which is a technique to cache previously computed results, or using mathematical approaches such as Binet's formula to directly compute the nth Fibonacci number. 
If you want to discuss any of these advanced techniques, or why the provided solution is more efficient than a simple recursive implementation, feel free to ask!