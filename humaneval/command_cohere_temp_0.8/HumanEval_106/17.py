```python
def f(n):
    # Initialize an empty list to store the final results
    result = []
    
    # Iterate through the range of numbers from 1 to n
    for i in range(1, n+1):
        # If the current number 'i' is even, calculate the factorial of 'i'
        if i % 2 == 0:
            result.append(factorial(i))
        # If the current number 'i' is odd, calculate the sum of numbers from 1 to 'i'
        else:
            result.append(sum(range(1, i+1)))
    
    # Finally, return the computed list of results
    return result

def factorial(n):
    # Implement factorial function using recursion
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

The function `f` takes an integer `n` as input and creates a list where the element at index `i` is either the factorial of `i` (if `i` is even) or the sum of numbers from 1 to `i` (if `i` is odd). This is achieved through a nested loop structure. The helper function `factorial` is implemented using recursion and calculates the factorial of a given number `n` by multiplying `n` with the factorial of `n-1`. 

This code can be tested by calling the `f` function with different values for `n` and verifying that the produced list corresponds to the description provided in the problem statement.