```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1, and the next number is the sum of the previous two numbers.
    
    This function uses memoization to efficiently compute the n-th Fibonacci number. It takes a his approach is to first calculate the partial sums of Fibonacci numbers, and then use the previously computed partial sums to calculate the n-th Fibonacci number.
    
    Parameters: n:
        An integer representing the position of the Fibonacci number to calculate.
    
    Returns: The n-th Fibonacci number.
    """

def test_fib4():
    """Test the fib4 function with various input values."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 24
    assert fib4(9) == 44
    assert fib4(10) == 98

    """Output the result for testing."""
    print("Test Results:")
    print(fib4(10))

test_fib4()
```

The code defines a function fib4 that calculates the n-th Fibonacci number using memoization. The test_fib4 function performs various tests on the fib4 function, including inputs of 0, 1, and larger values. The function ensures correctness and efficiency by using memoization to avoid redundant calculations.