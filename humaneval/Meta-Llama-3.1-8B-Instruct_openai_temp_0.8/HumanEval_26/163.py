```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        List[int]: A new list with duplicates removed.
    """
    
    # Create an empty dictionary to store the count of each number
    count_dict = {}
    
    # Create an empty list to store the result
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number is not in the dictionary, add it to the dictionary and the result list
        if num not in count_dict:
            count_dict[num] = 1
            result.append(num)
        # If the number is already in the dictionary, increment its count
        else:
            count_dict[num] += 1
    
    # Return the result list
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, this function is not very efficient as it has to create a dictionary and append to the result list for every number in the input list. We can improve the efficiency by using a different approach.

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        List[int]: A new list with duplicates removed.
    """
    
    # Create an empty list to store the result
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number is not in the result list, add it to the result list
        if num not in result:
            result.append(num)
    
    # Return the result list
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 2, 3, 4]
```

This function is more efficient because it only needs to check if a number is in the result list, which takes constant time on average. However, it doesn't keep the original order of elements.