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
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
This script defines a function 'f' that takes an input 'n', and returns a list according to the specification in the prompt. The script also defines a helper function factorial(n) which returns the factorial of 'n'. The 'f' function uses the factorial function to calculate the factorial of even indices and returns the sum of numbers from 1 to i for odd indices. The script passes the test cases described in the prompt.