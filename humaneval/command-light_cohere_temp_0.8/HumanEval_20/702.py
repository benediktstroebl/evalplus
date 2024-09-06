Here is the self-contained Python function that solves the problem you provided:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    from typing import List
    """
    # sorting the list
    sorted_numbers = sorted(numbers)

    # getting the first and second element in the sorted list
    first_element = sorted_numbers[0]
    second_element = sorted_numbers[1]

    # comparing the first elements and second elements
    if first_element < second_element:
        return first_element, second_element
    else:
        return second_element, first_element
```

This function accepts a list of numbers as input, sorts the list, and then returns the first and second closest elements in the sorted list. It uses the specified to check the first and second elements and returns them in order of smaller to larger number.

Note:  This function uses the typing module, which is a built-in Python module used for type hinting and static type checking. It's essential to import the module before using the type hints.