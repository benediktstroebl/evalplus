```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    duplicates = {x_num for _num in numbers if numbers.count(_num) > 1}
    return [i for i, _num in enumerate(numbers) if _num not in duplicates]}
    return [i for i, _num in enumerate(numbers) if _num not in duplicates]

# Test
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]
```
The remove_duplicates function takes a list of integers as input and removes all elements that occur more than once in the list. The duplicates are stored in a set and are filtered using the filter function. The output is a set of integers that do not appear more than once in the original list.