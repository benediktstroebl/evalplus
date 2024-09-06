```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(enumer()) if num > max_or_moment(numbers, num)]
 
def max_or_moment(numbers: List[int], max_element: int) -> int:
    current = max_element
    for num in numbers:
        if num > current:
            current = num
    return current
``` 
This Python code defines a function called rolling_max that generates a list of rolling maximum elements in a given list of integers. It utilizes a essential helper function max_or_moment to find the maximum element that appears after the current maximum element in the list.

You can test this code by calling the rolling_max function with a sample list of integers and print the result.