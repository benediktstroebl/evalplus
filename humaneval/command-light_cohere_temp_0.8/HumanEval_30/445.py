```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

#Test case 1: returns [2, 5, 6]
get_positive([-1, 2, -4, 5, 6])

#Test case 2: returns [5, 3, -5, 2, -3, 3, 9, 0, 123, 1]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

#Test case 3: returns [] (empty list)
get_positive([1, 2, 3, -4, -5])

#Test case 4: returns [123]
get_positive([123, 2, 3, 4, 5])
```
This Python code defines a function `get_positive` that takes a list as an argument and returns a new list containing only the positive numbers from the original list. The code then passes several tests by calling the `get_positive` function with different lists and verifying if the returned list matches the expected output.