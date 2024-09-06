```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It returns the n-th Fibonacci number. The base cases are handled efficiently, as the function returns n and n-1 for n equal to 1 and 2, respectively. For larger values of n, it recursively computes the sum of the (n-1)-th and (n-2)-th Fibonacci numbers, making sure the result is correct and conforming to the specification. 
The function can be tested by calling it with different values of n and comparing the results against the expected Fibonacci numbers.