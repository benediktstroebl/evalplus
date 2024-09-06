```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test
values_test = [1, 2, 'three', 3, 'four', 'five']
test_results = filter_integers(values_test)
print(test_results)  # Output: [1, 2, 3, four, five]
```
This script provides a function called `filter_integers` that accepts a list of values and returns a new list containing only the integers from the input. It uses the initial list comprehension to complete this task. 

Also, we can test the function using the code provided, which creates a new list with various values, then calls the `filter_integers` function to create a new list that only contains integers.