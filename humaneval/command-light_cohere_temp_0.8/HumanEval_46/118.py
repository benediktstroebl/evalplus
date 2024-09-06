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

# Example usage
test_fib = fib4(5)
print("Result:", test_fib)
```
The provided Python function, fib4, calculates the n-th Fibonacci number in the Fibonacci sequence using a loop-based approach. It begins by evaluating base cases for n equal to 0, 1, and 2, which yield 0, 0, and 2, respectively. Then, it employs recursive calls to compute Fibonacci numbers for larger values of n, summing the results to obtain the desired Fibonacci number. The example usage demonstrates how the function can be used to find the n-th Fibonacci number in a given range.

The result of the test_fib will be:
Result: 4