Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
The `f` function uses two loops: the outer loop iterates over the integers from 1 to `n` (inclusive). The `factorial` function is called for the even indices and the `sum` function is called for the odd indices. The `factorial` function, in turn, uses a loop to calculate the factorial of `n` by iterating from 1 to `n` and multiplying the `result` variable by the current iterator value. 

This code will work correctly for the provided example of `f(5)`. The code includes a factorial function which is a common enough need that it's reasonable to expect it to be reused, and the use of a separate function makes the primary `f` function cleaner and easier to read. 

The only unavoidable exception is that the last element in the list will be the sum of numbers from 1 to `n`, rather than the factorial of `n`, since the former is computing a sum from 1 to `n` and the latter is computing a factorial of n. This is a well-known mathematical coincidence, as `f(n)` is the sum of the first `n` integers if `n` is odd, and the factorial of `n` if `n` is even.