```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fib4 sequence is usually defined as 0, 1, 1, 2, ...
    n: int
    fib: [0, 1] = [0, 1]
    for _ in range(n):
        fib.append(fib[n-2] + fib[n-3])
    return fib[n - 1]

# Unit tests
def test_fib4():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 2
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

# Main function calling test suite
test_fib4()
```
The code defines a function fib4 that calculates the n-th Fibonacci number using an iterative approach. The function begins by initializing a list fib with the base Fibonacci numbers [0, 1]. It then enters a loop that iterates from n down to 1, appending the sum of the Fibonacci numbers at indices n-2 and n-3 to the list. The loop continues until then reaches 0, and the function returns the value at index n - 1.

The code also includes a set of unit tests, which use the assert statement to check that the fib4 function produces the correct Fibonacci numbers when given certain input values. 
Finally, the test_fib4 function is called, which executes the unit tests and verifies that the function is working correctly.