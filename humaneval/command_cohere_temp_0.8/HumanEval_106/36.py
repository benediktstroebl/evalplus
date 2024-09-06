Here is a Python script that solves the problem you have described:
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
The `f` function uses the `factorial` function to generate the appropriate list of numbers as per the problem statement. 
This code defines two functions: `f` takes an integer `n` as input and returns a list where each element is either the factorial of an even index or the sum of numbers from 1 to an odd index; the `factorial` function calculates the factorial of a given number `n` by multiplying `n` with all integers from 1 to `n`.

The code does not take any input from the user and instead outputs the list `li`, which stores the answers to the problem statement for different values of `n`. The `factorial` function is deterministic and calculates the factorial of a given integer `n` in `O(n)` time; the `f` function uses the `factorial` function and loops through all numbers from 1 to `n` and produces the answers to the problem statement in `O(n)` time. Therefore, the code operates in `O(n)` time and uses `O(1)` space.