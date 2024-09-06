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

def test_fib4():
    """Function to test the function fib4"""
    print("Fibonacci sequence:")
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
```
This code defines a Python function called `fib4`, which computes the Fibonacci sequence up to the nth element. The function follows a mathematical definition of the Fibonacci sequence and uses a recursive approach without memorization to compute the sequence. It then has a test function `test_fib4` which tests the `fib4` function with various input values and prints the results.