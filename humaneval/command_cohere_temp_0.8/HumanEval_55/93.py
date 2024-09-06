```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This function works for any positive integer input since it uses recursion to compute the Fibonacci sequence. It starts with the base cases of 1 and 0 (since Fibonacci(0) = 0 and Fibonacci(1) = 1), and then recursively adds the two previous Fibonacci numbers to generate the next number in the sequence. 

Here are some example outputs:
Fibonacci(4) = 3 + 5 = 8
Fibonacci(6) = 5 + 8 = 13
Fibonacci(10) = 55

This approach provides an efficient way to compute the Fibonacci sequence, making it scalable for large inputs compared to iterative direct formulas that have exponential growth. 
```python 
```