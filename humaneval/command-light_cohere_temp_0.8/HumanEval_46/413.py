```python
def fib4(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

#Test the function
def test_fib4():
    n = 7
    assert fib4(n) == 14  # This should be true

test_fib4()
```
The code defines a Fibonacci sequence function called fib4 which calculates the n-th element in the sequence. This is then a simple case where n is 0, 1, or 2 which returns the appropriate element. The else branch calculates the result by summing up the last 4 elements of the sequence. Then, the test_fib4 function tests the function by calling fib4 with the value n = 7 and asserts that the result is 14. The code is well-structured and contains a clear function with an accompanying test to ensure its correctness.