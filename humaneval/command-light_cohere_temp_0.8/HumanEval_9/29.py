```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the given moment in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # Implementing the rolling max function
    numbers = [x for x in numbers if x != float('-inf')]
    rolling_max_ = [x for _, x in enumerate(numbers)] if max(rolling_max_) == numbers[-1]:
        rolling_max_[-1] = max(rolling_max_)
        return rolling_max_[:-]  # Returning the list of rolling max elements

    # Unit tests
    numbers = [1, 2, 3, 4, 5]
    rolling_max(numbers)  # Output: [3, 4, 5]
    numbers = [float('-inf'), 1, 2, 3, 4, 5]
    rolling_max(numbers)  # Output: [1, 2, 3]
    numbers = [10, 20, 30, 40]
    rolling_max(numbers)  # Output: [40, 30, 20]
    ```
This Python script defines a function `rolling_max` that generates a list of rolling maximum elements in a given list of integers. The function first converts the dry the list to ensure only non-negative integers and then uses the `enumerize` function with a generator expression to generate the rolling max elements. The output of the function is then tested with different input arrays to ensure its correctness.