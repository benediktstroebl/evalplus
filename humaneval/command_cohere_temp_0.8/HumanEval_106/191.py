```python
def f(n):
    ans = []
    for i in range(1, n+1):
        if i % 2 == 0:
            ans.append(factorial(i))
        else:
            ans.append(sum(range(1, i+1)))
    return ans

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
This Python script defines two functions. The first function, f, accepts an integer n as input and returns a list populated with the result of a conditional expression. If the index i is even, the element in the list is the factorial of i. Otherwise, the element is the sum of numbers from 1 to i. The second function, factorial, accepts an integer n as input and returns the factorial of n, the product of all numbers from 1 to n. 

The example provided in the prompt leads to the following outcome:
```python
f(5) == [1, 2, 6, 24, 15]
```
This goal is successfully achieved by the script above, as the function f returns the expected list [1, 2, 6, 24, 15].