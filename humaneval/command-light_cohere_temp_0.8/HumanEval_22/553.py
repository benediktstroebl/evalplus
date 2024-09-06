```python
from typing import List

def filter_integers(values:
        return [x for x in values if type(x) == int]

# Test the function
values = [1, 2, 3, 'abc', {}, []]
result = filter_integers(values)
print(result)  # Output: [1, 2, 3]
```
This Python code defines a function called `filter_integers` that takes a list of values as an argument and returns a new list containing only the integer elements from the input. The function utilizes a filtering mechanism to iterate through the values and filter out any non-integer values. The test case demonstrates the value of the function by passing a sample list of values and outputting the resulting filtered list, which includes only the integers 1, 2, and 3 from the input list.