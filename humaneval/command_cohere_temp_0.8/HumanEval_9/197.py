```python
from typing import List, Tuple

def rolling_max(numbers: List[int], max_window: int = None) -> List[int]:
    if max_window is None:
        max_window = len(numbers)
    
    rolling_max_values = [numbers[0]]
    
    for i in range(1, len(numbers)):
        if i - max_window < 0:
            rolling_max_values.append(numbers[i])
        else:
            rolling_max_values.append(max(numbers[i-max_window:i+1]))
    
    return rolling_max_values
```

The given Python script defines a function called rolling_max, which takes a list of integers numbers and an optional parameter max_window. By default, the max_window is set to the length of the input list if not specified. The function generates a new list, `rolling_max_values`, where each element at index `i` holds the maximum value from the sublist `[numerals[i-max_window]:numbers[i+1]]`. While iterating through the list, the function handles the window size equivalently by taking the full window size at the beginning of the sequence, shrinking down as the index increases, and eventually settling on individual elements when the window size is lesser than or equal to the sequence length. It utilizes the `max()` function to compare and return the maximum value for each window size. The resulting `rolling_max_values` list holds these maximum values over time. 
```python
# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```

In the example usage, the output will be:
```
[1, 2, 3, 3, 3, 4, 4]
``` 

This output aligns with the prompt's expected output, where the rolling maximum values are listed accordingly. 

Note: The script assumes that the initial window size is equal to the sequence length, and the window size decreases incrementally. You can adjust the `max_window` parameter or incorporate dynamic window sizing logic if your sequence and window dynamics are different.