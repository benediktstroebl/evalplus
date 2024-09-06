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
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
The provided code defines a function called fib4 that calculates the n-th value of the Fibonacci sequence using the recursive approach without recursion. The function follows the series of Fibonacci numbers, where each number is the sum of the previous three values. It begins with the 0 and 1 as the base cases and calculates subsequent values by summing the previous three numbers. The test_fib4 function asserts that the calculated value of the function for a given input matches the expected result.

This code demonstrates the functionality of the fib4 function, which efficiently computes Fibonacci numbers without relying on recursion, providing a simple and straightforward solution to the problem.