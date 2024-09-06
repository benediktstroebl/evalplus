Here is a self-contained Python script with a function that checks if any two numbers in a given list are closer to each other than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold."""
    return any(x <= y for x, y in zip(numbers, numbers)) and numbers <= threshold


```
This function uses the **any** function and the **<=** operator to check if any two elements in the list are equal or less than the given threshold. The **zip** function is used to iterate over the two lists.