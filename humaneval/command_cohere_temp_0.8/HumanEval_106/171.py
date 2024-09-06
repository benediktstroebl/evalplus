Here is a Python script that implements the function f, as described in the problem:
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
The function f takes an integer n as input and creates a list where the element at index i is the factorial of i if i is even, or the sum of numbers from 1 to i otherwise. The factorial of i is calculated using the factorial function, which returns the factorial of n by multiplying the numbers from 1 to n. This script passes the test cases mentioned in the original problem description.