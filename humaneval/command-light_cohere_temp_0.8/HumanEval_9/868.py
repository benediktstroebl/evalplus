```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    Each element in the a list of integers will be tried as a potential maximum,
    and the maximum found will be appended until a new, larger 
    element is found and the max is updated.
    """

    test case:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([5, 6, 7, 8, 9, 10])
    []
    """
    l = [num for num in numbers if num > max_element]
    max_element = max(l, default=0)
    return [max_element] + rolling_max(numbers[len(l)::])
``` 
The code defines a function `rolling_max` that generates a list of the rolling maximum elements from a given list of integers. It uses list comprehension to filter out elements that are greater than the current maximum element and then uses the `max` function with default argument to get the current maximum element. 
The `rolling_max` function is then tested with a sample input list and the expected output is printed.