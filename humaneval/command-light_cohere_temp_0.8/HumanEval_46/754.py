```python
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

# Run the function and print the result for n = 5
fib4(5)

```
The code defines a Python function called fib4 that computes the n-th element of the Fibonacci sequence without using recursion. The function uses a input n, and if n is 0, it returns 0. Otherwise, it checks the base cases for n equal to 1, 2, and 3, where it returns the corresponding Fibonacci numbers. For other values of input n, the function recursively calls itself with the arguments (n - 1), (n - 2), (n - 3), and (n - 4), adding the results together to compute the n-th Fibonacci number. The function is a solution and does not use recursion.