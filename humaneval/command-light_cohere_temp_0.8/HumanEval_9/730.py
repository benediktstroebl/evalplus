```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling max elements found until a given moment in the sequence
    :param numbers: list of integers
    :return: list of integers
    """
    return [x for x, _ in sorted(enumer(numbers) for _ in range(1))][::-1:]

# Test Case 1: Basic Test
numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
assert list(result) == [max(numbers[::i+1]) for ::i in range(len(numbers)))]

# Test Case 2: Removing Duplicates
numbers = [1, 2, 3, 2, 3, 4, 4]
result = rolling_max(numbers)
assert len(result) == 6 and all(result != numbers[i] for i in range(6))

# Test Case 3: Custom Input
numbers = [5, 2, 8, 1, 10, 3, 6, 7, 9]
result = rolling_max(numbers)
assert len(result) == 10 and all(result >= numbers[i] for i in range(10))
```