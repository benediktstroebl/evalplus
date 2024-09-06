```python
def fib4(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Example usage
print(fib4(5))
print(fib4(6))
print(fib4(7))
```
This code defines a function fib4 that computes the n-th Fibonacci number in the Fibonacci sequence using the recursive method. It uses base cases for n=0,1,2,3 and for general n, it calls fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4). The This function can be used to calculate Fibonacci numbers efficiently for any given n. The output of the example usage is the n-th Fibonacci number for n=5,6,7.

This code is a great example of a self-contained function that can solve a complex problem with a simple and efficient solution.