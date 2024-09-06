```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements in the given sequence.
    Args: numbers (List[int]): Given sequence of integers
    Returns: List[int]: List of rolling maximum elements found until the given moment in the sequence.
    """
    list comprehension and slicing of the input list, using the rolling window strategy, to find the maximum elements in each window.
    """
list comprehension:
    max_window = [num for num in numbers[-1:] + [num] + numbers[:-2]]
    return [max(window) for window in max_window]

test_rolling_max:
List[int] = list(map(int, input(). neat_input))
def test_rolling_max(func):
    assert func(input_list) == output_list
    return
```