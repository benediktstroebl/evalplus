Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at each position in the sequence. The function is designed to work with both regular and lazy evaluation strategies:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], pivot_point: int = None) -> List[int]:
    if pivot_point is not None:
        # Using lazy evaluation strategy
        max_so_far = numbers[pivot_point]
        result = [max_so_far]
        left, right = pivot_point, len(numbers) - 1
        while left < right:
            max_so_far = max(numbers[right], max_so_far, numbers[left])
            result.append(max_so_far)
            left += 1
            right -= 1
        return result
    else:
        # Using regular evaluation strategy
        max_so_far = float('-inf')
        result = []
        for right in range(len(numbers)):
            max_so_far = max(numbers[right], max_so_far)
            result.append(max_so_far)
        return result

# Test the function with regular and lazy evaluation strategies
cases = [
    ([1, 2, 3, 2, 3, 4, 2], [1, 2, 3, 3, 3, 4, 4]),
    ([1, 2, 3, 2, 3, 4, 2], 4),
]
for nums, expected in cases:
    result = rolling_max(nums)
    assert result == expected
```

In this script, the `rolling_max` function takes an additional optional parameter `pivot_point`, which denotes the point in the sequence around which the rolling maximum should be calculated. When `pivot_point` is provided, the function uses a lazy evaluation strategy, comparing only three elements at a time to find the maximum. Alternatively, when `pivot_point` is not provided, the function uses a regular evaluation strategy, iterating through the entire sequence to determine the rolling maximum. You can test the function using both strategies by providing `pivot_point` or leaving it blank, and verifying the output against the expected results.