```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each subsequent number is defined as the sum of the two preceding ones.
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Example usage
fib = fib4(7)
print("The result is:", fib)
```
The code defines a Fibonacci function that calculates the n-th element of the Fibonacci sequence using the recursive formula. The function returns the value of the Fibonacci number based on the input n. The function handles invalid input values and returns 0 for them. The example usage demonstrates how to call the fib4 function and print the result.