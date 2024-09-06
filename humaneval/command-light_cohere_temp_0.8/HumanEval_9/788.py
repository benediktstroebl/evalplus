```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    A function to get the maximum element in a list, using rolling window approach
    """
    max_count = 0
    current_max = numbers[0]
    result = [current_max]
    
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        else:
            max_count += 1
            if max_count == len(numbers) - 1:
                current_max = numbers[num]
            else:
                current_max = numbers[num]
        
        result.append(current_max)
    
    return result
``` 
This function uses the rolling window approach to efficiently find the maximum element in a list.