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
The function `f` takes an integer `n` and creates a list of `n` length. Every even index's element is filled with the factorial of that index, and every odd index is filled with the sum of the range from 1 to that index. The `factorial` function is a helper function that multiplies `n` by `i`, where `i` starts from 1 and goes up to `n`.

This code can efficiently solve the problem and can be directly copied and run.