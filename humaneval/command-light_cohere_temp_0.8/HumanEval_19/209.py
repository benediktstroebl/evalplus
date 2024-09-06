```python
from typing import List
def sort_numbers(input_str: str) -> str:
    """Sorts numbers from smallest to largest
    Valid input: space-separated numbers from 0 to 9
    Returns: space-separated numbers sorted from smallest to largest"""
    input_str = input_str.
    numbers = list(map(int, input_str.sort(numbers))
    return ' '.join(numbers)
# Tests
input1 = 'three onefive'
input2 = 'two three four five six seven eight nine'
print(sort_numbers(input1))  # expected output: one three five six seven eight nine
print(sort_numbers(input2))  # expected output: two three four five six seven eight nine')
```