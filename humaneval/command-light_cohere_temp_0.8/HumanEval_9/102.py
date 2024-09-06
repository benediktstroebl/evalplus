```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.patch_sequence = [i for i, n in enumerate(numbers):  # Preprocessing to avoid duplicates
        numbers.seqmax_element = n
       i = numbers.max_elements  # i+1
        numbers.remove_duplicates = [numbers[i+1:] if numbers[i+1] > max_element else numbers[i]]]
        numbers.max_elements = max(numbers.remove_duplicates)
    sorted(numbers.max_elements)
    return sorted(numbers.max_elements)
```