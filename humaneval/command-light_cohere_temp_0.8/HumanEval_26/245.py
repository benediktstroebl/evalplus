```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.set()] # {set() = set(numbers)}
    ```  This function removes duplicate elements from the input list of integers and returns a new list with unique elements.  The set() is used to convert the list into a set and then it checks if each element is not in the set, ensuring that it's not a duplicate.  This result is list with unique elements.