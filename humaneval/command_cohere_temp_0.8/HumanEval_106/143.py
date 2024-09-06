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
This script defines two functions: 'f(n)' generates a list according to the specifications of the problem, and 'factorial(n)' calculates the factorial of a given number. The factorial is calculated by multiplying the result with each number from 1 to 'n' and the list is constructed by pairing the factorial for each even index with the sum of numbers from 1 to the odd index. This solves the problem and passes the provided test.