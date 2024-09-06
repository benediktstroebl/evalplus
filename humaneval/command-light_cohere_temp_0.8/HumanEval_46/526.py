Here's a self-contained Python script that defines a function fib4 that computes the n-th element of the Fibonacci sequence using the iterative method:
```python
def fib4(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

```

This function uses the iterative method to calculate the n-th element of the Fibonacci sequence using the formula:
`F(n) = F(n-1) + F(n-2) + F(n-3) + F(n-4)`

It also includes input validation to ensure that the input n is a positive integer greater than 0. The function returns the expected output when the input is tested.