Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def f(n):
    ls = []
    for i in range(1, n+1):
        if i % 2 == 0:
            ls.append(factorial(i))
        else:
            ls.append(sum(range(1, i+1)))
    return ls

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
The function f takes an integer n as input and creates a list where the index of the list corresponds to the value of the element. If the index is even, the element's value is the factorial of that index. If the index is odd, the element's value is the sum of numbers from 1 to that index. The factorial of a number is the product of all the numbers from 1 to that number. 

The `factorial` function calculates the factorial of a given number n. It starts with an initial value of one and then multiplies it with all numbers from 1 to n. The `f` function uses the `factorial` function to solve the problem. 

This script will solve the problem as requested in the markdown code block. It will create a list of size n, where the value of the element at index i is the factorial of i if i is even or the sum of numbers from 1 to i otherwise. 

The example input of 5 will return [1, 2, 6, 24, 15].