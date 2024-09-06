```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize Set to keep track of unique numbers.
    seen_numbers = set()

    # Initialize List to store the output.
    output = []

    # Loop through the input list
    for num in numbers:
        if num not in seen_numbers:
            seen_numbers.add(num)
            output.append(num)

    return output
```
Do you require any additional assistance with other coding problems or want to explore more Python concepts?