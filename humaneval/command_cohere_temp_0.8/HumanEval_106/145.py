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
This script defines two functions:
1. The `f` function takes an integer `n` as input and returns a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from 1 to `i` otherwise. This is achieved using a `for` loop that iterates through indices from 1 to `n`, and for each even index, it calculates the factorial and for each odd index, it calculates the sum of numbers from 1 to `i`. These values are then appended to the `ans` list.
2. The `factorial` function calculates the factorial of a given integer `n` by iterating through all numbers from 1 to `n` and multiplying them with the `result` variable, which should be initialized to 1.

Both functions are deterministic and will return the correct value given the input. The `f` function will return a list based on the specifications you provided.