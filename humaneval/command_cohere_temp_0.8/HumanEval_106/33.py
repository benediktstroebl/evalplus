Here is a Python script that implements the function `f` according to the problem statement:
```python
def f(n):
    li = []
    for i in range(1, n+1):
        if i % 2 == 0:
            li.append(factorial(i))
        else:
            li.append(sum(range(1, i+1)))
    return li

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
The `f` function uses the factorial function to generate the list according to the given problem statement. 
This code defines both functions and returns the list `li` in the `f` function.

However, since this is a self-contained code block, there are no unit tests to verify the implementation.