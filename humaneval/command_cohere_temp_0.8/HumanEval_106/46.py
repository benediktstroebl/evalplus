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
The code includes two functions: `f(n)` which is the function described in the problem, and `factorial(n)` which calculates the factorial of a given number. The code uses a list comprehension to create a list of size `n`, and then fills it according to the specifications of the problem, indexing from 0. 
The `factorial(n)` function is used to calculate the factorial of a number for the even indices of the `li` list. 

This code will solve the problem as required. Let me know if you would like any adjustments or additions!