Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
The `f` function uses the factorial function to create the list accordingly. 
The `factorial` function uses a simple loop to calculate the factorial of a number. 

This code will solve the given problem and return the requested list. 
The `f` function is self-contained and doesn't need any other externally imported function. 

The example passed as a parameter in the prompt is also correctly solved by this code.