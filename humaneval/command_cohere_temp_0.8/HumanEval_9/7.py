Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at different points in the sequence:
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

When you run this script with the example input, it will produce the following output:
```
[1, 2, 3, 3, 3, 4, 4]
```

This output shows the rolling maximum elements found at different points in the sequence `[1, 2, 3, 2, 3, 4, 2]`. The function updates the 'max_so_far' value as it iterates through the list, ensuring that the maximum value is accurately computed and reflected in the `result` list.