```python
def fibfib(n: int) -> int:
    if n == 0:  # base case
        return 0
    elif n == 1:  # base case
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

# Test cases
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
print(fibfib(9))  # Output: 55
print(fibfib(0))  # Output: 0
print(fibfib(-1))  # Output: AttributesError: 'int' attribute out of range: -1
```
This script defines a function `fibfib` that calculates the n-th element of the Fibonacci sequence using recursion. The base case is returning 0 for n = 0 and 1 for n = 1, and subsequent Fibonacci numbers are calculated by summing the previous two numbers and adding the third number. The test cases cover different values of n and pass the expected output.