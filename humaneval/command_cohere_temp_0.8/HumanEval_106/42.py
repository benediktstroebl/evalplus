```python
def f(n):
    # Initialize an empty list to hold the results
    result = []
    
    # Iterate through the range of numbers from 1 to n
    for i in range(1, n + 1):
        # If the current number 'i' is even, calculate its factorial
        if i % 2 == 0:
            result.append(factorial(i))
        # If the current number 'i' is odd, calculate its sum from 1 to i
        else:
            result.append(sum(range(1, i + 1)))
    
    # Return the list of computed values
    return result

def factorial(n):
    # Implement factorial function for n
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

The function `f` takes an integer `n` as input and creates an empty list `result` to store the computed values. It then iterates through the range of numbers from 1 to `n`, and for each number `i`, it checks if `i` is even. If it is, it calculates the factorial of `i` and appends it to `result`. If `i` is odd, it calculates the sum of numbers from 1 to `i` and appends that to `result`. Finally, it returns the list `result` containing the computed values based on the described conditions. 

The factorial function `factorial(n)` is also implemented to calculate the factorial of a given number `n` by iterating through the range from 1 to `n` and multiplying the values together.