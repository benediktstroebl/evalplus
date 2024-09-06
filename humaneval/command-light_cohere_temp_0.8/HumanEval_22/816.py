```python
from typing import List

def filter_integers(values:
    """
    filtered_numbers = [num for num in values if isinstance(num, int)]
    return filtered_numbers

# Test cases
values1 = [1, 2, 3, 'abc', {}, [5])
values2 = [1, 2, 3, 4, 'five', [6])

print(filter_integers(values1))  # Output: [1, 2, 3, 'abc', 5]
print(filter_integers(values2))  # Output: [1, 2, 3, 4, 'five', 6]
```  This code defines a function `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input.