Here is a Python script that solves the problem you have described:
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
The `f` function generates a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from `1` to `i` otherwise. The `factorial` function calculates the factorial of a given number using a loop.

To verify the functionality, you can call `f` with `n=5` and compare the returned list with `[1, 2, 6, 24, 15]`, as mentioned in the accompanying text.