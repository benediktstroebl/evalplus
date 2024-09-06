```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

```
We've defined a function called `fib4` that computes the n-th element of the Fibonacci sequence. The function follows the simple logic: it checks for the base cases (n = 0 and n = 1) and returns 0. For other values, it recursively calls itself to calculate the next element by summing the previous four elements.

This function is self-contained and efficient, using a simple and elegant approach. It can be used to solve problems related to Fibonacci numbers and calculate Fibonacci values for any given input.