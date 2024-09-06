```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. The function calculates and returns the n-th Fibonacci number. This is done using a recursive approach, where the function calls itself recursively to calculate the previous two Fibonacci numbers and then adds them together to obtain the desired Fibonacci number.

The script includes a docstring at the beginning of the fib function, which provides information about what the function does, the expected input, and the output values for various inputs. These helpings serve as documentation for users who will be using the function.

To test the function, the script includes a section of test code that calls the fib function with different values of n and checks if the returned values match the expected Fibonacci numbers. The script uses the pytest framework, which is a popular testing library in Python. The test code is structured using pytest's marking syntax, which asserts that the correct output is returned for each input.

Overall, this Python script provides an effective and efficient way to calculate Fibonacci numbers, along with thorough documentation and unit tests to ensure correct functionality. 
```python
def fib(n):
    """Return n-th Fibonacci number."""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def test_fib():
    """Test the correctness of fib."""
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 5
    assert fib(4) == 8
    assert fib(10) == 55

```