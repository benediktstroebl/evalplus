Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at any given point in time in the sequence:
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

# Test Cases
numbers_list = [1, 2, 3, 2, 3, 4, 2]
result_1 = rolling_max(numbers_list)
print(result_1)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines the `rolling_max` function, which uses a variable `max_so_far` to keep track of the maximum value encountered thus far. The function then generates a new list `result` where each element `result[i]` is the maximum value of the first `i+1` elements in the input list. It iterates through the list, updating `max_so_far` and appending to `result` accordingly. The provided test case demonstrates the function's behavior and produces the expected output.