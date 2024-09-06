Here is a Python script that solves the given problem:
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

The function `f` takes an integer `n` and creates a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from `1` to `i` otherwise. The `factorial` function is also provided to ensure the correctness of the `f` function. 

This code should pass all related tests, and the function correctly solves the problem statement.