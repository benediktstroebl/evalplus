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
This script defines two functions:
1. The `f` function takes an integer `n` as input and returns a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from `1` to `i` otherwise. This list is created and filled using a list comprehension and a `for` loop. The `if` statement in the `for` loop checks if the current index `i` is even or odd and assigns the appropriate value to the list.
2. The `factorial` function calculates the factorial of a given integer `n` by multiplying all numbers from `1` to `n`. It uses a `for` loop and the result is initialized to `1` and multiplied by each number in the loop. The final result is the factorial of `n`.

The code works as follows:
- The `f` function takes an integer `n` as input and returns a list `li` where each element is computed based on the described conditions.
- The `factorial` function calculates the factorial of a given integer `n` using a loop.

This code is self-contained and solves the problem statement, as the `f` function returns the required list, and the `factorial` function provides the necessary helper functionality.