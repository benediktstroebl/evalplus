Here is a Python script that solves the problem you have described:
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
The `f` function generates a list where the i-th element is the factorial of i if i is even, or the sum of numbers from 1 to i otherwise. To do this, it iterates through each index of the list, using the `factorial` function to calculate the factorial of each even index and the `sum` function to calculate the sum of each odd index. 
The `factorial` function calculates the factorial of a given number by iterating through all numbers from 1 to that number and multiplying them by the result variable, which is initialized to 1.

This code should work for the given problem and also passes the example test case. It returns a list of size n, where the value of the element at index i is the factorial of i if i is even or the sum of numbers from 1 to i otherwise.  For example, f(5) would return [1, 2, 6, 24, 15].  If you have any further questions or would like me to explain any part of the solution in more detail, let me know!