```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(numbers, reverse=True) if num > numbers[numbers.find_max()]]
``` 
This script defines a function `rolling_max` that calculates the rolling maximum element in a list. In this approach, the function utilizes the sorted() method with reverse=True to sort the list in descending order. Then, it applies the list comprehension to filter and retain only the elements that are greater than the current maximum element found using the `find_max()` method. 

This function effectively generates a new list with the rolling maximum elements found in the original list.