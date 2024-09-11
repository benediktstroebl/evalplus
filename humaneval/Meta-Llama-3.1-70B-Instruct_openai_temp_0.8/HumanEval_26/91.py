```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an OrderedDict to keep track of element counts and maintain insertion order
    counts = OrderedDict()
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    # Filter out elements that occur more than once
    result = [num for num, count in counts.items() if count == 1]
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```
Alternatively, you can use a list comprehension with a conditional expression to achieve the same result in a more concise way:

```python
from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    counts = Counter(numbers)
    return [num for num in numbers if counts[num] == 1]

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```