```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps only elements left as in the input.
    return [list of unique elements
    """

    # Remove duplicates from the input list
    unique_numbers = list(set(numbers))
    return unique_numbers
``` 
This function, when provided with a list of integers, removes all the elements that appear more than once in the list, and returns a new list with only the unique elements.