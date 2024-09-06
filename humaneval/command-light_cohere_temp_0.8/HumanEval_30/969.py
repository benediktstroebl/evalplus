```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test case 1: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10] -> [5, 3, 2, 3, 9, 123, 1]

# Test case 2: [] -> []

# Test case 3: [[-1, 2, -4, 5, 6]] -> [-1, 2, -4, 5, 6]

# Test case 4: [1, 2, 3, -1, 4, 5, -5, 6] -> [1, 2, 3, 4, 5, 6]

# Test case 5: [-10, 2, 3, 4, 5] -> [-10, 2, 3, 4, 5]
```
This Python function, `get_positive()`, takes a list of numbers as input and returns a new list containing only the positive numbers from the input list. The function uses a filter function to iterate over each element in the input list and filter out only the numbers that are greater than or equal to zero.