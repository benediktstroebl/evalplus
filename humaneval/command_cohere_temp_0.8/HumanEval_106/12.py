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
This code defines the `f` function as requested, using a loop and the factorial function to generate the correct values for the list. The factorial function calculates the factorial of a given number `n` by iterating through numbers from 1 to `n` and multiplying them by the `result` variable, which should be initialized to 1. The final list is returned with the calculated values. 
This approach ensures that the function f returns the desired list as specified in the problem statement.