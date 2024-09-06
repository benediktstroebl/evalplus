```python
def fib4(n: int):
    """
    The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. Fibonacci numbers are
    4-number sequence: 0, 1, 1, 2, 3, 5, 8, ...
    The Fibonacci function calculates the n-th Fibonacci number in the sequence using a simple formula.
    """
    function fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

def test_fibonacci(n: int):
    """
    Validate the input.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Test the function with various values of n
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")

# Test the function with different values of n
test_cases = [5, 6, 7]

for test_case in test_cases:
    test_fibonacci(test_case)

``` 
This code defines a function called fibonacci which calculates the n-th Fibonacci number using a recursive formula. The function test_fibonacci is then used to validate the input and test the function with different values of n.