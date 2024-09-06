```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_roll = 0
    current = numbers[0]
    result = [current]
    
    for num in numbers[1:]:
        if num > current:
            current = num
        max_roll = max(max_roll, current)
    
    result.append(current)
    return result

numbers = [1, 2, 3, 2, 3,4]
print(rolling_max(numbers))  # expected output: [1, 2, 3, 3, 3, 4, 4]
``` 
This code defines a rolling_max function that takes a list of integers and returns a new list where each element is the maximum element from the original list after that element. It tests by comparing each number in the list with the current maximum element and updating both the maximum element and the current maximum element accordingly.