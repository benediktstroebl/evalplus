Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at any given moment in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_list = [max_so_far]
    
    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
            max_list.append(max_so_far)
        
    return max_list
```

The script uses a simple approach of maintaining a variable `max_so_far`, which is the maximum value encountered so far. Initially, it's set to the first element of the list. The function also maintains a `max_list`, which is a list that contains the rolling maximum value up to each point in the sequence. As new elements are encountered, it updates the `max_so_far` and accordingly updates the `max_list`. 

This approach ensures that the rolling maximum value up to each point in the sequence is recorded in the `max_list`.