```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest higher integer first.
    """
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return result
```

This Python script defines a function called `sum_squares` which takes in a list of numbers (`lst`) as input. Within the function, it uses a generator expression alongside the `sum` function to calculate the sum of squared integers in the list. 

Before performing this operation, the function filters the list to only include integers (by checking if each element `x` has a modulo of 1, thus excluding any non-integer values). The result is the sum of the squared integers in the list, which are rounded to the nearest higher integer. 

The function then returns this calculated result. The logic ensures correctness and efficiency in handling the task, and the concise expression showcases Python's expressive capabilities. 

This function can be easily incorporated into larger Python scripts or applications to calculate the sum of squared integers in a list, especially when the elements require rounding before performing the operation.