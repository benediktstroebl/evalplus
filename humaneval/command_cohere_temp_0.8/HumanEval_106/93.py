Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def f(n):
    out = []
    for i in range(1, n+1):
        if i % 2 == 0:
            out.append(factorial(i))
        else:
            out.append(sum(range(1, i+1)))
    return out

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
This script defines a function f(n) that returns a list according to the specification. The factorial(n) function is also provided to calculate the factorial of a given number, which is used in the f function. The overall time complexity of this code is O(n).

The factorial function has a time complexity of O(n) as it iterates through the range from 1 to n and multiplies the values together, and the main f function has a time complexity of O(n) as it iterates through the range from 1 to n and performs a constant-time operation for each element.