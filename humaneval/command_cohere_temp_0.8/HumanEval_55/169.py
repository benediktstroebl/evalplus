```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It returns the nth Fibonacci number. The base cases are handled with the conditional statement `if n <= 1`, where it returns n if n is either 1 or 0, which are the first two numbers in the Fibonacci sequence. If n is greater than 1, it recursively calls itself with the arguments n-1 and n-2, and adds the results to produce the next Fibonacci number. This script provides a straightforward implementation of the Fibonacci sequence without storing previous results, making it suitable for computing individual Fibonacci numbers efficiently. 
The Python markdown cell displays the code with a grey background and black code, making it easier to distinguish against the surrounding text.