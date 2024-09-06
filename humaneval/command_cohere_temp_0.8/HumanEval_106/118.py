Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def f(n):
    ls = []
    for i in range(1, n+1):
        if i % 2 == 0:
            ls.append(factorial(i))
        else:
            ls.append(sum(range(1, i+1)))
    return ls

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
The function f returns a list where the element at index i is the factorial of i if i is even, or the sum of numbers from 1 to i otherwise. We define the factorial function using a loop to calculate the product of all numbers from 1 to n.