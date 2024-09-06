Here's a Python script that contains a function called `rolling_max` that takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at different points in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    result = [max_so_far]
    
    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```

When you run the example, the output will be:
```python
[1, 2, 3, 3, 3, 4, 4]
```

This script defines the `rolling_max` function, which uses a `max_so_far` variable to keep track of the maximum element encountered thus far. The `result` list is populated with this maximum element as we traverse the input list. The function returns the `result` list, which contains the rolling maximum elements.