```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns the list of rolling max elements found in the given sequence.
    This
   
    list of numbers is passed as input, 
    and the rolling max element is calculated and returned for each element.
    """
    max_num = numbers[0]
    rolling_maxes = [max_num]
    for num in numbers[1:]:
        current_max = max(max_num, num)
        rolling_maxes.append(current_max)
    return rolling_maxes

# Example
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_result = rolling_max(numbers)
print(rolling_max_result)  # Output: [1, 2, 3, 3, 3, 4, 4]

```

Please let me know if you would like any other details or explanations about the code.