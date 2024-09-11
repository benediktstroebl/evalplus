```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The list of integers with duplicates removed.
    """
    seen = {}  # Dictionary to store seen elements
    result = []  # List to store the result
    
    for num in numbers:
        # If the number is not in the'seen' dictionary, add it to the dictionary and the result
        if num not in seen:
            seen[num] = True  # Set the value to True, we don't care about the value, only the key
            result.append(num)
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. It uses a dictionary `seen` to keep track of the elements it has seen so far, and a list `result` to store the final result. The function iterates over the input list, and for each number, it checks if the number is in the `seen` dictionary. If it's not, it adds the number to the `seen` dictionary and the `result` list. Finally, it returns the `result` list.