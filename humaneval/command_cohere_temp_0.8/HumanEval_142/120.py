```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This Python script defines a function called `sum_squares` that takes a list of integers as input. It iterates through each element in the list and squares elements when the index is a multiple of 3 and cubes elements when the index is a multiple of 4 but not a multiple of 3. The function then returns the sum of all modified elements in the list. 

Let's break down the code:
- `result = 0` initializes a variable result to store the sum of modified list elements.
- The `for i, num in enumerate(lst)` loop iterates through each element in the list using the `enumerate` function, which automatically 
assigns the index `i` and value `num` of each list element.
- `if i % 3 == 0` checks if the index `i` is a multiple of 3. If true, it squares the `num` and adds it to the `result`.
- `elif i % 4 == 0 and i % 3 != 0` checks if the index `i` is a multiple of 4 but not a multiple of 3. If true, it cubes the `num` 
and adds it to the `result`.
- The `return result` statement returns the accumulated sum of modified list elements. 

The script is self-contained and does not rely on any external definitions or variables. 

You can test the function by calling it with various input lists and verifying the output against the specified requirements.

**NOTE**: If you have chunks of code that are more than 3 lines, consider using indents for readability instead of the customary solution of using nested loops. This significantly improves code readability and maintainability.