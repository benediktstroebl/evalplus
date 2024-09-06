```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    From a list of integers, remove all elements that occur more than once.
    Returns a unique elements as a new list.

    """
    remove duplicates:
    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    return new_list

tests:
    input_list = [1, 2, 3, 2, 4, 3, 2]
    expected_output = [1, 3, 4]
    remove_duplicates(input_list)
    assert input_list == expected_output
    ```