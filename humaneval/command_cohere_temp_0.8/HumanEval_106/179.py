Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def f(n):
    ans = []
    for i in range(1, n+1):
        if i % 2 == 0:
            ans.append(factorial(i))
        else:
            ans.append(sum(range(1, i+1)))
    return ans

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num
```
This script defines a function 'f' that takes an input 'n', and returns a list based on the given markdown specification. It also includes a nested function 'factorial' to calculate the factorial of a given number. The 'f' function constructs the output list by alternating between the factorial and the sum for each odd and even index 'i', starting from 1. 

Note: the code assumes that the length of the list indicated by the `n` parameter does not exceed limits in terms of memory and execution time. In cases where this may be a concern, considerations should be made to handle such scenarios.