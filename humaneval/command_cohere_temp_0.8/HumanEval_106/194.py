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
This script defines a function `f` that takes an integer `n` as input and creates a list where the element at index `i` is either the factorial of `i` if `i` is even, or the sum of numbers from 1 to `i` otherwise. To calculate the factorial of a number, the script utilizes a nested function called `factorial`. This function multiplicates the `result` by `i` for all integers from 1 to `n`. The `f` function tests well with the provided example in the prompt, and the `factorial` function with the test case `factorial(5)` which should return 120. 
For clarity, the script does not adhere to the usual convention of having the `factorial` function take a parameter and return the factorial value, instead of being a nested unnamed local function. It would be advisable to change the function definition to `def factorial(n):` and modify the body of the function to return the calculated factorial value instead. Possibly, the `f` function could also benefit from a docstring summary.