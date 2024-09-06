```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This function uses a recursive approach to calculate the Fibonacci sequence, which is an efficient way to compute the sequence for small or moderate values of `n`. It employs an intuitive approach that aligns with the sequence's definition, providing a clear understanding of the algorithm's logic. 

Here are some usage examples to demonstrate the function's behavior:
```python
 >>> fib(1)
1
>>> fib(8)
21
>>> fib(10)
55
```
This should return the 1st, 8th, and 10th Fibonacci numbers respectively.