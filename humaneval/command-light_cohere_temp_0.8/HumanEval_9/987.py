```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns the list of rolling maximum elements found until the given moment in the sequence
    >>> rolling_max([1, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4]
    >>> rolling_max([5, 10, 2, 8, 20, 10, 5])
    [20, 10, 10, 8, 10]
    """
    numbers.sort()
    max_element: int = float('inf')
    rolling_max_elements = [max_element]
    while True:
        current_element = numbers[0]
        numbers.remove(current_element)
        if numbers:
            next_element = numbers[-1]
            numbers.insert(0, next_element)
            max_element = next_element
            rolling_max_elements.append(max_element)
        else:
            break
    return rolling_max_elements
``` 
Do you have a solution to the problem?