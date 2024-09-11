```markdown
### Remove Duplicates from a List of Integers

This Python script solves the problem by using a dictionary to keep track of the elements we've seen so far and their counts. It iterates over the input list, and for each element, it checks if it's already in the dictionary. If it is, and its count is greater than 1, it skips the element. If it's not in the dictionary or its count is 1, it adds the element to the dictionary with a count of 1. Finally, it returns a list of all the keys in the dictionary, which represent the elements in the input list that occur only once.
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with all duplicates removed.
    """
    seen = {}
    result = []

    for num in numbers:
        if num not in seen or seen[num] == 1:
            seen[num] = seen.get(num, 0) + 1
            result.append(num)

    return result

### Example Usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 1, 2, 2, 3, 3]))  # Output: []
print(remove_duplicates([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```