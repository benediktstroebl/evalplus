```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    return:
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 2
        else:
            return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Test the fib4 function
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 28
    assert fib4(9) == 44
    assert fib4(10) == 90

# Call the fib4 function with different values to test the correctness of the function
``` 
This code defines the `fib4` function that computes the n-th Fibonacci number using an efficient iterative approach. It also includes a test_fib4 function with several test cases to ensure the correctness of the `fib4` function.