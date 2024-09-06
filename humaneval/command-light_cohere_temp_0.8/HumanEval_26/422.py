Here is a self-contained Python script that defines and implements the `remove_duplicates` function:
```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicate integers from the input list.
    Args:
        list of integers
    Returns:
        list of unique integers.
    """
    def remove_duplicates(numbers):
        seen = set()
        result = []
        for num in numbers:
            if num not in seen:
                seen.add(num)
                result.append(num)
        return result
    ```

# Example usage:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]
```

This script provides a self-contained function that solves the problem of removing duplicate integers from a given list.  It follows a type hint and test-driven development approach.