```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of integers with all elements that occur more than once removed.

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an empty dictionary to store the count of each number
    count_dict = {}
    
    # Iterate over the input list to count the occurrence of each number
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Create a new list to store the result
    result = []
    
    # Iterate over the input list again to add numbers with count 1 to the result list
    for num in numbers:
        if count_dict[num] == 1:
            result.append(num)
    
    # Return the result list
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script uses a dictionary to count the occurrence of each number in the input list. Then, it iterates over the input list again to add numbers with a count of 1 to the result list. The result list is then returned. The time complexity of this solution is O(n), where n is the length of the input list, making it efficient for large lists.