Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def f(n):
    l = []
    for i in range(1, n+1):
        if i % 2 == 0:
            l.append(factorial(i))
        else:
            l.append(sum(range(1, i+1)))
    return l

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
The function f returns a list of size n, such that the value of the element at index i is the factorial of i if i is even, or the sum of numbers from 1 to i otherwise. The factorial of i is calculated using the factorial function.  For example, f(5) == [1, 2, 6, 24, 15].