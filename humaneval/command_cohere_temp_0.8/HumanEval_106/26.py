Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
The `f` function uses two loops: the outer loop iterates over the indices from 1 to `n`, and the inner loop (only used for odd indices) iterates from 1 to `i` to calculate the sum of numbers from 1 to `i`. The `factorial` function calculates the factorial of `n` using a loop that multiplies the current `i` by `result`.

You can verify the correctness of the implementation by running the provided tests. 
The test cases are designed to check the behavior of the `f` function for different input values and ensure its compliance with the problem statement. Each test case verifies whether the returned list corresponds to the specified conditions, which involves checking the value of the elements and verifying if they match the expected outcomes.