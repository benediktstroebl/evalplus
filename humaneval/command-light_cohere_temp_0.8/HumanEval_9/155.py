Here's the improved Python code:
```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.max = [max(numbers)
    current = numbers[0]
    result = [current]
    
    for num in numbers[1:]:
        if num > current:
            current = num
        result.append(current) 
    return result
```

This code uses the `max()` function to find the maximum element in the list and then iterates through the list, updating the current maximum element as it's larger than the previous one. The code then generates a list of rolling maximum elements found until the moment in the sequence.