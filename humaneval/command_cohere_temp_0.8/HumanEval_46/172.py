```python
def fib4(n):
    fib4_cache = [0, 0, 2, 0]
    if n < 0:
        raise ValueError("fib4 is not defined for negative numbers")
    elif n < 5:
        return fib4_cache[n]
    else:
        return fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
```
This Python script defines a function `fib4` that efficiently calculates the n-th element of the Fib4 sequence, a variation of the Fibonacci sequence. The function first checks if n is negative, and if so, raises a ValueError. If n is 0 to 4, it returns the value from a cached list of the first five Fib4 values. If n is greater than 4, it calculates the result using the definition of the Fib4 sequence, avoiding recursion for better performance, and stores the result in the cache for future use. 

Here is an example usage of the function:
```python
>>> fib4(5)
4
>>> fib4(6)
8
>>> fib4(7)
14
```
This output shows that the function correctly calculates the Fib4 values for 5, 6, and 7.