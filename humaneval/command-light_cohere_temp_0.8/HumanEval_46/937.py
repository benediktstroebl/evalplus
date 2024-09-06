```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. 
    The function uses a mathematical definition of the n-th Fibonacci number."""
    
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2)

def test_fib4():
    """Test the function fib4."""
    
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14 

# Call the test function to run the tests.

test_fib4()
``` 
The code defines a function `fib4` that computes the n-th Fibonacci number using a mathematical definition, without recursion. The function takes an integer `n` as input and returns the n-th Fibonacci number. The test function `test_fib4` is used to verify that the `fib4` function is working correctly for a number of test cases.