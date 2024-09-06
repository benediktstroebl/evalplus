```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements in the given sequence.
    """ 
    numbers = sorted(numbers)
    max_element = numbers[0]
    rolling_max_list = [max_element] + [max(num, max_element) for num in numbers[1:]]
    return rolling_max_list

# Unit tests
numbers = [1, 2, 3, 4, 5]
assert Rolling_max(numbers) == [3, 4, 5, 5]

numbers = [1, 2, 3, 3, 4]
assert Rolling_max(numbers) == [3, 3, 4, 5]

numbers = [1, 2, 3, 4, 4]
assert Rolling_max(numbers) == [2, 3, 4, 5]

numbers = [1, 2, 3, 2, 3]
assert Rolling_max(numbers) == [1, 2, 3, 3]
```