Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
The `f` function uses the factorial function to generate the list according to the given problem description. The `factorial` function calculates the factorial of a given number `n` by iterating through the numbers from `1` to `n` and multiplying them together. The result is initialized to `1`, and each number is multiplied by the result iteratively. The final result is the factorial of the given number.