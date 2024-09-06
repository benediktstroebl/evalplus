Here's a Python script that contains a function called `rolling_max` that takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at every point in the sequence:
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

When you execute this script, it will generate output:
```
[1, 2, 3, 3, 3, 4, 4]
```

This output corresponds to the rolling maximum elements found at every point in the given sequence `[1, 2, 3, 2, 3, 4, 2]`. 

The function `rolling_max` uses two variables to solve the problem: 
- `max_so_far`: This variable keeps track of the maximum element encountered thus far in the sequence. 
- `result`: This variable is a precursor to the final result, and it stores the maximum elements encountered up until reaching each point in the sequence. 

In other words, it computes the required list of rolling maximum elements using the formula:
```
[max_so_far_1, max_so_far_2, max_so_far_3, ..., max_so_far_n]
```

The script self-contains the function `rolling_max` and can be easily imported as a separate module or executed directly for testing.