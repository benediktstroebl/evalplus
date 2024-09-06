```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Generate a list of rolling max elements from the given list of integers 
    until a given moment in the sequence is achieved.
    """
    list of rolling max elements = []
    for i in range(len(numbers)):
        current_max = numbers[i]
        while True: 
            # Calculate the maximum element seen so far 
            current_max_element = max(rolling_max[::-1], current_max)
            if current_max_element == numbers[i]:
                break; 
            rolling_max.append(current_max_element)
        return rolling_max
    """
    assert all(rolling_max(numbers[:5]) == numbers[:5]), "The list generated doesn't match the input"
    return rolling_max
```
The code first creates an empty list to store the rolling max elements. Then, it iterates through the loop through the input list, where the maximum element seen so far is compared to the current element to determine the rolling max element. The code then appends the maximum element to the list until the current element matches the input element, at which point the loop exits.