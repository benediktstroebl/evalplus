Here is a self-contained Python script with a function that solves the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    Returns a tuple with the two closest numbers and their relationship.
    """
    Python function
    test case:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4])
    return ((2.0, 1.0, 1.0))
    test another test case:
    >>> find_closest_elements([1.0, 2.0, 4.0, 5])
    return ((4.0, 1.0, 3.0))
test case:
    >>> find_closest_elements([1.0, 1.0, 2.0, 2])
    relationship= 1.0, 2.0, 4.0)
return (4.0, 1.0, 3.0)
test case:
    >>> find_closest_elements([1.0, 1.0, 2.0, 3])
   return (1.0, 1.0, 3.0)
test case:
    >>> find_closest_elements([1.0, 2.0, 2.0, 3]) == ((1.0, 1.0, 3.0))
test case:
    >>> find_closest_elements([1.0, 2.0, 3.0, 2]) == ((1.0, 2.0, 3.0))
    test case

```
This script defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two numbers in the list that are closest to each other. The function uses the typing `List` and `Tuple` to define the function and test cases correctly.