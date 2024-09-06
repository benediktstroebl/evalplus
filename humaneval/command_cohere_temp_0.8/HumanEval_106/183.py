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
This Python script defines two functions. The first function, f, accepts an integer n as input and returns a list populated with the result of a ternary operation, dependent on the parity of the index number. If the index is even, the element is set to the factorial of the index, calculated using a nested function. If the index is odd, the element is set to the sum of the numbers within the range of 1 to the index. The second function, factorial, accepts an integer n and returns the factorial of n, calculated by iterating through the range from 1 to n and multiplying the values together. 

Here is an example call to the `f` function with the argument `5`:
```python
f(5)
```

This would invoke the function f with the argument 5, and return the list [1, 2, 6, 24, 15].