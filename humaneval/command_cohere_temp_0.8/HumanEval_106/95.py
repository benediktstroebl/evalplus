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
This script defines a function 'f' that takes an input 'n', and returns a list according to the specification. The nested function factorial calculates the factorial of a given number 'n', which is used to populate the list accordingly. The code self-contained and does not require any additional imports or dependencies.