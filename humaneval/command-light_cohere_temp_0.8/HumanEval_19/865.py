```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    """
    assert sorted(numbers) == 'one three five', "Test 1 failed"
    assert numbers == 'three one eight five', "Test 2 failed"
    assert numbers == 'three two four five', "Test 3 failed"
    assert numbers == 'zero three six seven', "Test 4 failed"
    assert numbers == 'one two three four', "Test 5 failed"
    return " succeeded"
```