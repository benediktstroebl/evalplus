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

# Tests:
assert f(1) == [1]
assert f(2) == [1, 2]
assert f(5) == [1, 2, 6, 24, 15]
```
The `f` function takes an `n` parameter and returns a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from `1` to `i` otherwise. The `factorial` function is also included in the code and helps us calculate the factorial of a given number `n`. 

The tests assert the correctness of the solutions for inputs `1`, `2`, and `5`, ensuring that the function `f` is correctly implemented.  This code demonstrates how we can use loops and functions to solve problems that involve conditional logic and create efficient and reusable code.