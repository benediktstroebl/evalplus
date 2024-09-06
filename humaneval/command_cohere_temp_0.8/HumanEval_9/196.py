Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at every point in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = []
    for i in range(len(numbers)):
        max_so_far = max(numbers[i], rolling_maxes[-1]) if rolling_maxes else numbers[i]
        rolling_maxes.append(max_so_far)
    return rolling_maxes

# Test Cases
numbers_list = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers_list))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script utilizes a list `rolling_maxes` to store the rolling maximum elements and updates it iteratively based on the input list `numbers`. The output of the provided test case matches the expected result. You can add more test cases to validate the function's behavior further.