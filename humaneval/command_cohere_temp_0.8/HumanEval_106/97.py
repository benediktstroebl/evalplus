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
This Python script defines two functions. The first function, f, accepts an integer n as input and returns a list populated with results computed based on the parity of their respective indices. If the index is even, the value corresponds to the factorial of that index, computed using the factorial function. If the index is odd, the value is the sum of numbers ranging from 1 to that index. 

The factorial function, on the other hand, accepts an integer n and returns the factorial of that number, computed by multiplying all integers from 1 to n together. 

Please note that the factorial function is reused from a previously provided solution.