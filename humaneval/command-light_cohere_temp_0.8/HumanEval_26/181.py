```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from a list of integers and return a new list without duplicates.
    """
    list of integers without duplicates is:
    [1, 2, 3, 4]
    """
    # Initialize an empty set to store unique elements
    unique_elements = set()

    # Initialize an empty list to store the results
    result = []

    # Iterate over the input list
    for num in numbers:
        # If the element is already in the unique_elements set, it's a duplicate
        if num in unique_elements:
            continue
        # Add the element to the unique_elements set
        unique_elements.add(num)

        # Add the element to the result list
        result.append(num)

    # Return the list without duplicates
    return result
``` 
This function uses a set to efficiently store unique elements and a list to store the results. The function iterates through the list, and for each element, it checks if it is already in the set. If the element is not in the set, it adds it to both. If the element is already in the set, it continues to the next element.