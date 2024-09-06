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
This Python script defines two functions. The first function, f, accepts an integer n as input and returns a list populated with values ranging from 1 to n, calculated using a nested loop. This list boasts factorials of even values and summations of consecutive integers for odd values. The second function, factorial, is tasked with calculating factorials, employing a loop to multiply integers from 1 to n.