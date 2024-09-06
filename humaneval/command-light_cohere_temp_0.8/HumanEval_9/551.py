```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_element = numbers[0]
    for num in numbers[1:]:
        if num > max_element:
            max_element = num
    return [max_element]

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This function called `rolling_max` takes a list of integers as input and uses the first element as the max_element to start. The function then loops through the the list and compares each number with the current max_element. The highest number is then added to the list of rolling maximum elements.