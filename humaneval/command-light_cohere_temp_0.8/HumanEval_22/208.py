```python
from typing import List

def filter_integers(values:
        return [x for x in values if isinstance(x, int)]

# Test the function with a variety of inputs
test_values = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
test_results = filter_integers(test_values)

print("Test Results:", test_results)
```
This Python script defines a function named `filter_integers` that filters out any non-integer values from a given list. The function utilizes the `isinstance()` function to check if each value in the list is an instance of `int`. It returns a new list containing only the integer values. 

The script then applies this function to a list of test values and prints the results.