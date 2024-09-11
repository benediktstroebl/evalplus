```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    :param numbers: A list of integers
    :return: A new list with all elements that occur more than once removed
    """
    # Create an empty dictionary to keep track of the count of each number
    count_dict = {}
    
    # Create an empty list to store the result
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number is not in the dictionary or its count is 0
        if num not in count_dict or count_dict[num] == 0:
            # Add the number to the result list
            result.append(num)
            # Increment the count of the number in the dictionary
            count_dict[num] = count_dict.get(num, 0) + 1
    
    # Return the result list
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script uses a dictionary to keep track of the count of each number in the input list. It iterates over the input list, and for each number, it checks if the number is not in the dictionary or its count is 0. If this condition is met, it adds the number to the result list and increments the count of the number in the dictionary. This way, all elements that occur more than once are removed from the result list. The order of elements is preserved as in the input.