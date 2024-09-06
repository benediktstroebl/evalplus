```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each successive number is defined as the sum of the two preceding ones. 
    The sequence starts with 0 and 1, and the next number is the sum of these two numbers.
    """
    previous_fib = 0
    current_fib = 1
    
    """Add the current Fibonacci number to the sum of the two previous numbers to calculate the next Fibonacci number."
    
    while n > 0:
        previous_fib = current_fib
        current_fib = current_fib + previous_fib
        n -= 1
    
    return current_fib

#Test case 1
def test_fib4(n: int):
    assert fib4(5) == 4  # Should return 4
    assert fib4(6) == 8  # Should return 8

#Test case 2
def test_fib4(n: int):
    assert fib4(7) == 14  # Should return 14

#Test case 3
def test_fib4(n):
    assert fib4(8) == 24  # Should return 24

#Test case 4
def test_fib4(n):
    assert fib4(9) == 44  # Should return 44

#Test case 5
def test_fib4(n):
    assert fib4(10) == 50  # Should return 50
```
The `fib4` function takes an integer `n` as input and returns the n-th Fibonacci number. The function uses a efficient method that avoids recursion, instead, it adds the current Fibonacci number to the sum of the two previous numbers to calculate the next Fibonacci number. The test cases validate the` the function`'s ability to generate Fibonacci numbers correctly for different input values.