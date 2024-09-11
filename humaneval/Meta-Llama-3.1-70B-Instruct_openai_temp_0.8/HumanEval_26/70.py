```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an OrderedDict to store the count of each number
    count_dict = OrderedDict()
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Create a new list with numbers that occur only once
    unique_numbers = [num for num, count in count_dict.items() if count == 1]
    
    return unique_numbers


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([5, 5, 5, 5, 5]))  # Output: []
print(remove_duplicates([7, 8, 9, 10, 11]))  # Output: [7, 8, 9, 10, 11]
```

Alternatively, you can use a defaultdict from the collections module to simplify the code:

```python
from typing import List
from collections import defaultdict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create a defaultdict to store the count of each number
    count_dict = defaultdict(int)
    for num in numbers:
        count_dict[num] += 1
    
    # Create a new list with numbers that occur only once
    unique_numbers = [num for num, count in count_dict.items() if count == 1]
    
    return unique_numbers


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([5, 5, 5, 5, 5]))  # Output: []
print(remove_duplicates([7, 8, 9, 10, 11]))  # Output: [7, 8, 9, 10, 11]
```

Both versions of the function work correctly, but the second one is a bit more concise and uses the defaultdict to avoid the need for an if-else statement to initialize the count for each number.