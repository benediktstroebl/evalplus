```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with duplicates removed.
    """
    seen = set()  # Set to keep track of seen numbers
    result = []  # List to store the result
    
    for num in numbers:
        if num not in seen:  # Check if the number is seen before
            seen.add(num)  # Add the number to the seen set
            result.append(num)  # Add the number to the result list

    return result


# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```