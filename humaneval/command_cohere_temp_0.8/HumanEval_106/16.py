```python
def f(n):
    # Initialize an empty list to store the final results
    result = []
    
    # Iterate through the values from 1 to n in increments of 2
    for i in range(1, n+1, 2):
        # If the current value is even, calculate the factorial of i
        if i % 2 == 0:
            result.append(factorial(i))
        # Otherwise, calculate the sum of numbers from 1 to i
        else:
            result.append(sum(range(1, i+1)))
    
    # Ensure the list has a length of n by padding with None values
    return result + [None] * (n - len(result))

def factorial(n):
    # Initialize the result to 1
    result = 1
    
    # Iterate through the values from 1 to n
    for i in range(1, n+1):
        result *= i
    
    return result
```

The code includes two functions: `f(n)` that constructs the list according to the problem statement, and `factorial(n)` which is used to calculate the factorial of a number. 

The `f(n)` function first creates an empty list to store the results, then iterates through numbers from 1 to `n` with an increment of 2 using a `for` loop. 

If the current number is even, it calculates the factorial of that number and appends it to the list. Otherwise, it calculates the sum of numbers from 1 to the current number and appends it to the list. 

Finally, it returns the list, padding it with `None` values if necessary to ensure it has a length of `n`. 

You can use the `factorial(n)` function to calculate the factorial of a number `n` by simply calling it and passing `n` as an argument. 

This code demonstrates how to solve the problem using Python by defining a function `f` that takes an integer `n` as input and returns a list where the even indices are populated with the factorial of the corresponding value, and the odd indices are populated with the sum of numbers from 1 to the corresponding value, thereby achieving the desired list according to the problem statement.