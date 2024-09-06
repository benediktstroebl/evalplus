Here is a Python script that solves the problem you have described:
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
The `f` function takes an integer `n` as input and creates a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from `1` to `i` otherwise. The `factorial` function is also included to calculate the factorial of a given number `n`. This code defines the necessary functions and follows the example provided in the prompt. 

You can test this function by calling `f(5)` which should return the list `[1, 2, 6, 24, 15]` as mentioned in the prompt.