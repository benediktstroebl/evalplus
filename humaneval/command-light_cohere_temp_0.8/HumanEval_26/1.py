Here's a self-contained Python function that solves the problem you described:

```python
from typing import List

def remove_duplicates(numbers: List[int]):
    # Initialize set to store unique integers
    unique_set = set(numbers)
    
    # Convert set back to list
    unique_numbers = list(unique_set)
    
    return unique_numbers
```

The provided code defines a function named `remove_duplicates`, which takes a list of integers (`numbers`) as input and returns a new list containing only unique integer occurrences. The code achieves this uniqueization by converting the input list into a set and then converting the set back into a list, which effectively removes duplicate elements. The resulting list contains only unique integers from the original input.