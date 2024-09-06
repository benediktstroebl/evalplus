Here is a Python script that implements the function f in a way that is consistent with the given description:
```python
def f(n):
    r = []
    for i in range(1, n+1):
        if i % 2 == 0:
            r.append(factorial(i))
        else:
            r.append(sum(range(1, i+1)))
    return r

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
The function f returns a list of size n, where the value of the element at index i is the factorial of i if i is even, or the sum of numbers from 1 to i otherwise. The factorial of i is calculated by multiplying the numbers from 1 to i. This is achieved by utilizing the factorial helper function, which returns the factorial of a given number. This is then used to calculate the appropriate value for each index in the list.