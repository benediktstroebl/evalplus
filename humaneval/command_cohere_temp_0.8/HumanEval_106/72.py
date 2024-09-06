Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def f(n):
    # Initialize an empty list to store the results
    result = []
    # Iterate through the range of numbers from 1 to n
    for i in range(1, n+1):
        # If the current number is even, calculate the factorial of that number
        if i % 2 == 0:
            result.append(factorial(i))
        # If the current number is odd, calculate the sum of numbers from 1 to that number
        else:
            result.append(sum(range(1, i+1)))
    # Return the list of results
    return result

def factorial(n):
    # Initialize the result to 1
    result = 1
    # Iterate through the range of numbers from 1 to n
    for i in range(1, n+1):
        # Multiply the result by the current number
        result *= i
    # Return the factorial of n
    return result

# Example usage
print(f(5))
```
This script defines a function `f` that takes an integer `n` as input and creates a list where the even indices contain the factorial of that index and the odd indices contain the sum of the range from 1 to that index. The factorial of a number is calculated by multiplying the numbers from 1 to that number. The script also defines a helper function factorial that calculates the factorial of a given number. The example used in the problem statement would print the following output:
```
[1, 2, 6, 24, 15]
```
This satisfies the problem statement's example, as the list contains the appropriate values at each index.