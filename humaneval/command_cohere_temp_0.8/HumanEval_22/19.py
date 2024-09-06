```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result
```

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out values that are not of type `int`. It uses **List Comprehension** with the `isinstance()` function to iterate through the input list and checks if each element is an instance of the `int` class, if so, it appends that element to the `result` list. Finally, it returns the `result` list containing only the integers from the input list. 

Here's how you can use the above function to filter out the integers from the given sample test cases:
```python
test_list = ['a', 3.14, 5]
print(filter_integers(test_list))  # Output: [5]

test_list2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(test_list2))  # Output: [1, 2, 3]
```