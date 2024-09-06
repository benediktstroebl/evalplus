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
This Python script defines a function 'f' that takes an input 'n', and returns a list according to the specification in the prompt. The script also defines a helper function factorial() that calculates the factorial of a given number 'n'. The 'f' function utilizes the 'factorial' function to calculate the factorial of even indices, and uses a sum operation to calculate the sum of numbers from 1 to i for odd indices.