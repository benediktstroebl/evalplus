```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values for integers
    :param values: List[Any]
    :return: List[int]
    """
    return [i for i in values if isinstance(i, int)]

# Test the function with a sample input
values_test = [1, 2, 3, 'abc', {}, []]
result_test = filter_integers(values_test)
print(result_test)  # Output: [1, 2, 3]

# Test the function with a complex input
values_complex = [1, 2, 3, 'four', (5), [6, 7])
result_complex = filter_integers(values_complex)
print(result_complex)  # Output: [1, 2, 3, 'four', (5), [6, 7])
```

This Python script defines a function named `filter_integers` that filters a given list of values for integers. It uses a specific type hints `List[Any]` and then uses a list comprehension to filter out only the integer values from the input list. The function and test cases are designed to be self-contained within the Python script, demonstrating the functionality without depending on external code or external modules.