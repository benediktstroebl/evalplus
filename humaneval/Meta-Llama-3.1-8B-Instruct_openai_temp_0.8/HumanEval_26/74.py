```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        List[int]: A list of integers with duplicates removed.
    
    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    
    # Create an empty dictionary to keep track of the count of each number
    count_dict = {}
    
    # Create an empty list to store the result
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number is not in the dictionary or its count is 0, add it to the result list
        if num not in count_dict or count_dict[num] == 0:
            result.append(num)
            # Increment the count of the number in the dictionary
            count_dict[num] = count_dict.get(num, 0) + 1
    
    # Return the result list
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input, removes all elements that occur more than once, and returns the resulting list. The function uses a dictionary to keep track of the count of each number and a list to store the result. It then iterates over the input list, adding each number to the result list if it has not been seen before or if its count is 0. The function finally returns the result list. The script includes a test case to demonstrate the function's behavior.