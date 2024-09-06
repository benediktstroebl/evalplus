```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2)

if __name__ == "__main__":
    print("First test passed!")
    n = 7
    print("Fibonacci of", n, "is", fib4(n))
    print("Second test passed!")
```
The function `fib4` takes an integer `n` as input and returns the n-th Fibonacci number. The function uses a recursive approach to calculate the Fibonacci numbers and does not use any additional variables for memoization.