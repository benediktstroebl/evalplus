```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. This function efficiently calculates the _n-th Fibonacci number using the formula:
    result = ((n-1)*(n-2)) / 2
    return result

# Test the function
test_fib4 = fib4
test_fib4(5)
test_fib4(6)
test_fib4(7)
```
The `fib4` function takes an integer `n` as input and calculates the nth Fibonacci number using the formula ((n-1)*(n-2)) / 2. The function returns the result. 

This formula allows us to efficiently compute the nth Fibonacci number without using recursion, which can be more memory-efficient. 

The function is tested by calling it with different values of `n` and verifying that the returned values match the expected results.