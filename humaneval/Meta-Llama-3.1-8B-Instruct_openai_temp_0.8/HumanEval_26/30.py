```markdown
## Remove Duplicates from a List of Integers
### Problem Statement
From a list of integers, remove all elements that occur more than once.
Keep order of elements left the same as in the input.

### Solution

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from a list of integers.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers with duplicates removed. The order of remaining elements
        is kept the same as in the input list.

    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()  # Keep track of seen numbers to avoid duplicates
    result = []  # Store the result

    for num in numbers:  # Iterate over the input list
        if num not in seen:  # If the number is not seen before
            seen.add(num)  # Mark it as seen
            result.append(num)  # Add it to the result

    return result  # Return the result
```

### Example Use Cases

```python
# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]

# Another example
numbers = [5, 5, 5, 5, 5, 6]
print(remove_duplicates(numbers))  # Output: [6]
```
```

This solution uses a set (`seen`) to keep track of the numbers that have been seen so far. For each number in the input list, it checks if the number is in the `seen` set. If not, it adds the number to the `seen` set and appends it to the result list. This way, duplicate numbers are avoided and the original order is preserved.