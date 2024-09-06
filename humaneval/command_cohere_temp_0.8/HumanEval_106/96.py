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

# Tests:
print(f(5))
# [1, 2, 6, 24, 15]
```
The function `f` takes an integer `n` as input and creates a list of `n` elements. Each element in the list is computed based on the following rules:
If the index `i` is even, the element in the list is set to the factorial of `i`. 
If the index `i` is odd, the element in the list is set to the sum of numbers from `1` to `i`. 

The `factorial` function is also included to calculate the factorial of a given number `n` by iterating through all numbers from `1` to `n` and multiplying them. The code works as expected and returns the solution to the problem request. Gor the example input of `5`, the function returns the list `[1, 2, 6, 24, 15]`, which satisfies the requirement.  This approach captures the requested functionality in a straightforward manner. 
If there are any test cases you would like to see added or any further functionality you'd like included, don't hesitate to ask.