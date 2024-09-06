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

def main():
    test_fib4()

``` 
The code defines a `fib4` function that computes the n-th Fibonacci number in the Fibonacci sequence using the formula: `nth Fibonacci number = sum(2 previous Fibonacci numbers). The function handles an `if` statement to determine whether the function correctly computes the Fibonacci number for a given input `n`. 
The `test_fib4` function then checks the output of `fib4` for a series of test cases, and asserts that the function's output matches the expected result. 

The `main` function then calls the `test_fib4` function to run the test suite and verify that the function is working correctly.