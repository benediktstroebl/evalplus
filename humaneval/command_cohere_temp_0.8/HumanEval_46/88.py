```python
def fib4(n: int):
    if n < 0:
        raise ValueError(" fib4 is not defined for negative numbers")
    elif n < 4:
        return n
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
```
This code defines a function `fib4` that efficiently calculates the n-th element of the Fib4 sequence, given an integer n. It checks for invalid input and provides an error message for negative input values. The base cases are defined for n=0, n=1, n=2, and n=3, where the function returns 0 or the input value. For larger n, it recursively computes the Fib4 value by summing the previous three elements in the sequence.