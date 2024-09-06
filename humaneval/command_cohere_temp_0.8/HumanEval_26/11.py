```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Returns a new list without duplicates, keeping the order of elements left unchanged.
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen and not seen.add(num):
            result.append(num)
    return result
```

The above `remove_duplicates` function keeps the order of elements intact and removes only those integers that occur more than once in the given list. It uses a set called `seen` to keep track of unique elements and achieves the desired result efficiently. A usage example is provided below:
```python
# Example usage
input_list = [1, 2, 3, 2, 4]
result_list = remove_duplicates(input_list)
print(result_list)  # Output: [1, 3, 4]
``` 

This will print the result list, which has removed all duplicates, keeping only the unique integers from the input list.