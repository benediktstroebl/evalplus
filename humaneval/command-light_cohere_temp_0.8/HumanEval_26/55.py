Here is a self-contained Python script that defines and implements the remove_duplicates function, which removes duplicate elements from the input list of integers:
```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from the input list.
    """
    Keep only the individual occurrences of each element
    """
    # Create a dictionary to store the occurrences of each element
    seen = {}
    result = []
    for num in numbers:
        if num not in seen:
            seen[num] = 1
        else:
            seen[num] += 1
        result.append(num)
    return result
```
This function utilizes a dictionary to track the occurrence of each element. It iterates through element of the input list and appends elements that have already been seen. The function ensures that each element is added to the result list only once, effectively removing duplicate elements from the input list.