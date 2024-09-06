```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from the list of integers.
    Input: numbers is a list of integers.
    Returns: unique integers list.
    """
"""
    # create a new list and remove duplicates
    new_list = list(set(numbers))
    # return the new list with integers only
    return new_list

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4, 2, 5, 6]
    # test the function
    test_result = remove_duplicates(numbers)
    print(test_result)
```

This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the unique integers. The function achieves this removing duplicates by first converting the input list into a set and then creating a new list by extracting the unique elements from the set. The test_result variable is used to store the test input and the function is tested to ensure it works correctly.