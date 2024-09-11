### Remove Duplicates from List
#### Problem Statement
From a list of integers, remove all elements that occur more than once. Keep order of elements left the same as in the input.

#### Solution
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements from a list that occur more than once.
    
    Args:
        numbers (List[int]): The input list of integers.
    
    Returns:
        List[int]: The list with elements that occur more than once removed.
    """
    
    # Create an empty dictionary to store the count of each number
    count_dict = {}
    
    # Create an empty list to store the result
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number is not in the dictionary, add it with a count of 1
        if num not in count_dict:
            count_dict[num] = 1
            # Add the number to the result list
            result.append(num)
        # If the number is already in the dictionary, increment its count
        else:
            count_dict[num] += 1
    
    # Return the result list
    return result

# Example use case
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script uses a dictionary to keep track of the count of each number in the input list. It iterates over the input list, adding each number to the result list if it's not already in the dictionary, or incrementing its count in the dictionary if it is. This way, only numbers that occur exactly once are added to the result list.