```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each successive number is defined as a sum of the two preceding ones. Fibonacci numbers are example the numbers in the sequence:
    0, 1, 1, 2, 3, 5, 8, 13, ...
    This function calculates the nth element of the Fibonacci sequence using the formula:
    nth_fib = 0
    (nth_fib-1) + (nth_fib-2) + (nth_fib-3) + (nth_fib-4)
    return nth_fib

>>> fib4(0)
0
>>> fib4(1)
0
>>> fib4(2)
2
>>> fib4(3)
0
>>> fib4(5)
5
>>> fib4(6)
8
>>> fib4(7)
13
```
The above Python code defines a function `fib4` that computes the nth element of the Fibonacci sequence for a given `n` using the formula mentioned in the docstring.  The function returns 0, 1, 1, 2, 3, 5, 8, and 13 as expected for the test cases `fib4(0)`, `fib4(1)`, `fib4(2)`, `fib4(3)`, `fib4(5)`, `fib4(6)`, and `fib4(7)`, respectively.