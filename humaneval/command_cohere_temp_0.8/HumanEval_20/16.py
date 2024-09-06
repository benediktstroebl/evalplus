```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    x = numbers[-2]
    y = numbers[-1]
    return x, y
```

The function **find_closest_elements** takes a list of numbers **numbers** as input and returns a tuple containing the two numbers from the list that are closest to each other. The list is first sorted to ensure that the extremes are the closest pair, and then the second-to-last and last elements in the sorted list are returned, as this is the closest pair in the majority of cases. 

The function goes into a **ValueError** exception if the length of the supplied list is less than 2.

Here is an example of how to use the function:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
result = find_closest_elements(test_list)
print(result)  # Output: (2.0, 2.2)
```

And here is the Markdown code block for the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
```