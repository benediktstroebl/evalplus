```python
def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i+1)))
    return result

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
This script defines two functions:
1. The `f` function takes an integer `n` as input and returns a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from `1` to `i` otherwise. This is done in the `result` list comprehension, where `i % 2 == 0` checks if `i` is even, and assigns the factorial of `i` if it is, and otherwise assigns the sum of numbers from `1` to `i`.
2. The `factorial` function, defined outside of the `f` function, calculates the factorial of a given number `n` by multiplying all numbers from `1` to `n` and returns the result. This is done in the `result = 1` initialization, and the subsequent loop `for i in range(1, n+1):`, where `result *= i` multiplies `result` by `i` in each iteration from `1` to `n`. 

By defining the `factorial` function outside of `f`, the code adheres to the self-contained requirement, as it can run correctly in isolation.