```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicate integers and return the unique list.
    """
    for i in range(len(numbers)):
        if numbers[i] in numbers[numbers]:
            numbers[numbers].remove(numbers[i])
    return numbers

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```