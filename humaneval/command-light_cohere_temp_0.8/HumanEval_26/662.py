```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize an empty set to store unique integers
    unique_integers = set()
    
    # Initialize an empty list to store the unique integers
    result = []
    
    for num in numbers:
        if num not in unique_integers:
            unique_integers.add(num)
            result.append(num)
    
    return result
``` 
This function uses the Python 'set' and 'append' methods to remove duplicate elements and return the unique integers as a list. It ensures the test list is empty, creates a 'set' to store unique integers, and then iterates through the input list, adding each element to the set. The 'set' method automatically removes duplicate elements, and the 'append' method adds the unique elements to the result list.