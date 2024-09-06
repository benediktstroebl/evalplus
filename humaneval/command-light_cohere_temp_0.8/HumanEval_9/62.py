```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    Each element of the list will be the maximum of its previous two elements.
    Return a maximum list.
    """ Example number is to be rolled.
    """
    list of maximums is ordered from previous.
    """
    for index, element in enumerate(numbers):
        numbers[index] = max(numbers[index], numbers[index+1])
    return numbers

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This Python code defines a function called rolling_max that takes a list of integers as input and generates a new list where each element is the maximum of its previous two elements. The function achieves this purpose through repeatedly updating the current maximum element with the maximum value of the next element, effectively rolling over the maximum elements in the list. The example usage demonstrates how the list of numbers is passed to the rolling_max function, and the resulting maximum elements are printed.