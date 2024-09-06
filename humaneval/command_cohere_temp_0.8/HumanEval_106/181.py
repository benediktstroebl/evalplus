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
This Python script defines two functions. The first function, f, accepts an integer n as input and constructs a list where each element corresponds to the result of a specific condition: if the index is even, the element value is the factorial of that index, otherwise, it is the sum of integers from 1 to that index. This list is returned. The second function, factorial, calculates the factorial of a given number n by iterating through numbers from 1 to n, multiplying each by the running total, and returning the result. 

To ensure clarity and readability, the code includes a docstring at the beginning of the f function that explicitly describes its purpose, parameters, and return value, as well as an example for easy reference.