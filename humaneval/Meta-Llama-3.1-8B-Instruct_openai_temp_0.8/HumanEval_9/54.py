```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers: A list of integers.

    Returns:
    A list of rolling maximum elements.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize an empty list to store the rolling maximum elements
    rolling_max_list = []
    
    # Initialize the maximum element as the first element in the list
    max_element = numbers[0]
    
    # Iterate over each element in the list
    for num in numbers:
        # If the current element is greater than the maximum element, update the maximum element
        if num > max_element:
            max_element = num
        # Append the maximum element to the rolling maximum list
        rolling_max_list.append(max_element)
    
    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

Alternatively, we can use a more concise and Pythonic way to solve the problem using the built-in `max` function and a list comprehension:

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers: A list of integers.

    Returns:
    A list of rolling maximum elements.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [max(numbers[:i+1]) for i in range(len(numbers))]

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```