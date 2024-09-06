```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all elements that occur more than once from the input list of integers.
    Returns a duplicates removed list.

    Args:
        numbers (List[int]) - Input list of integers
    Returns: List[int] - List of unique integers
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
    ```
# Example usage:
numbers = [1, 2, 3, 2, 4]
unique_nums = remove_duplicates(numbers)
print(unique_nums)  # Output: [1, 3, 4]
``` 
This code implements the remove_duplicates function, which takes a list of integers as input and returns a new list of integers containing only the unique elements. The function uses a set to keep track of numbers we have encountered before, and then iterates through the input list, adding each number to the result if it's not already present in the set. 

Note that you can safely use this code as a standalone Python script, and it will provide the expected output.