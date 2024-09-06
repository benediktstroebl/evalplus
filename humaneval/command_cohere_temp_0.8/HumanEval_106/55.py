Here is a Python script that implements the function f in a way that is consistent with the problem description:
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
The function f accepts an integer n as input and creates a list li where each element is the factorial of i if i is even, or the sum of numbers from 1 to i if i is odd. This is achieved through the use of a for loop that iterates through numbers from 1 to n, and a helper function factorial that calculates the factorial of a given number. This code passes the tests outlined in the prompt: f(5) returns [1, 2, 6, 24, 15].