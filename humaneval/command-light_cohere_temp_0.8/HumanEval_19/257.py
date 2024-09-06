```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return sorted(numbers.split())
sorted_nums: List[int] = []
    for num in numbers:
        num = int(num)
        sorted_nums.append(num)
    return ' '.join(str(sorted_nums))

# Example usage:
>>> sort_numbers('three one five')
'one three five'

```