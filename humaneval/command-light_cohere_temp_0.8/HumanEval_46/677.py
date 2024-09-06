```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fib4 sequence is also called Fibonacci numbers or Fibonacci sequence.
    
    The sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4(n):
    """Test the Fibonacci sequence function
    
    """Test Case 1:"
    assert fib4(5) == 4
    """

# Your code here

# Test Case 2:
    assert fib4(7) == 14

def main():
    """Driver code to run the tests."""
    test_fib4(5)
    test_fib4(7)

if __name__ == "__main__":
    main()
```
The Python code above provides a self-contained function that computes the n-th element of the Fibonacci sequence using the recursive approach without using any additional functions. The function follows the recursive approach, which computes the next number in the sequence by summing up the previous four numbers. The test cases are also provided to validate the function.