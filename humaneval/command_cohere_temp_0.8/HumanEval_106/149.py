Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def f(n):
    li = [0] * n
    for i in range(1, n+1):
        if i % 2 == 0:
            li[i-1] = factorial(i)
        else:
            li[i-1] = sum(range(1, i+1))
    return li

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
The `f` function uses two nested loops to populate the list `li` with the required values, while the `factorial` function calculates the factorial of a given number `n`. 

This solution has a time complexity of O(n^2) due to the nested loops, but it should be noted that the factorial calculation within the `f` function only occurs for even values of `i`, resulting in a more efficient algorithm than if the factorial were calculated for all values.