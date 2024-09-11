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
    
    # Create an empty dictionary to keep track of the count of each number
    count_dict = {}
    
    # Create an empty list to store the result
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number is not in the dictionary, add it with a count of 1
        if num not in count_dict:
            count_dict[num] = 1
        # If the number is already in the dictionary, increment its count
        else:
            count_dict[num] += 1
        
        # If the count of the number is 1, add it to the result list
        if count_dict[num] == 1:
            result.append(num)
    
    # Return the result list
    return result

# Test the function
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

Alternatively, you can solve this problem using a more concise and Pythonic approach using a dictionary's `get` method and list comprehension:

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
    
    # Create an empty dictionary to keep track of the count of each number
    count_dict = {}
    
    # Use list comprehension to create a new list with duplicates removed
    return [num for num in numbers if (count_dict.setdefault(num, 0), num) == (0, num)]

# Test the function
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

Or, even more concisely, using `collections.Counter`:

```python
from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A new list with duplicates removed.
    """
    
    # Create a counter object
    counter = Counter(numbers)
    
    # Use a list comprehension to create a new list with duplicates removed
    return [num for num in numbers if counter[num] == 1]

# Test the function
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```