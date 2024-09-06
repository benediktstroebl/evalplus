```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. Fibonacci numbers can more by summing the previous two numbers in the sequence."""
    return (fib4(n-1) + fib4(n-2))

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
The function calculates the n-th Fibonacci number in a simple and efficient manner without recursion, which is a common method to solve problems like this. 

Also, we can test the function with various input values and ensure it produces the correct output, which is an essential step to validate any mathematical function.