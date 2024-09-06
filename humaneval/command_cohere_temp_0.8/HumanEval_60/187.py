```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to `n` (inclusive). It uses the `sum` function to add up all the values in the `range` of numbers from 1 to `n`, inclusive, and returns the result. 

The script includes a docstring with information about the function, including how to use it with examples, and what kind of value it returns.

This function is useful for summing a range of integers and can be called with an integer argument to get the sum of integers from 1 to that number. 

You can use it in your code by calling the function with a value of `n` to get the sum of integers from 1 to `n`. 
```python
result = sum_to_n(6)
print(f"The sum of integers from 1 to 6 is: {result}")
```
This will give an output:
```
The sum of integers from 1 to 6 is: 21
```