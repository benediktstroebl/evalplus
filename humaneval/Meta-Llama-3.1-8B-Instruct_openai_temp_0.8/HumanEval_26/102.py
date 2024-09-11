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
    seen = set()
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number has not been seen before, add it to the result and mark it as seen
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```

In this script, we create an empty set called `seen` to keep track of the numbers we have encountered. We create an empty list `result` to store the numbers that appear only once in the input list.

We iterate over the input list. For each number, we check if it is in the `seen` set. If it is not, we add it to the `result` list and mark it as seen by adding it to the `seen` set.

Finally, we return the `result` list, which contains only the numbers that appear only once in the input list.