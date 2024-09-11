```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        List[int]: A list of integers with duplicates removed.
    """
    # Create an ordered dictionary to keep track of the count of each number
    count_dict = OrderedDict()
    
    # Iterate through the list to count the occurrence of each number
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Use list comprehension to filter out numbers with more than one occurrence
    result = [num for num, count in count_dict.items() if count == 1]
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 3, 4]
```

Alternatively, you can also use a more concise solution with a dictionary comprehension and a list comprehension:

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
    # Create a dictionary to keep track of the count of each number
    count_dict = {num: numbers.count(num) for num in set(numbers)}
    
    # Use list comprehension to filter out numbers with more than one occurrence
    result = [num for num in numbers if count_dict[num] == 1]
    
    # Remove duplicates from the result while preserving order
    result = list(dict.fromkeys(result))
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 3, 4]
```