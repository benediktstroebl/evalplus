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
The `f` function uses a list comprehension to create a list with `n` elements, where each element is the result of the corresponding condition in the problem statement. The `factorial` function is also included to calculate the factorial of a given number `n`. The result of the `f` function for `n = 5` is `[1, 2, 6, 24, 15]`, which matches the example in the problem statement.